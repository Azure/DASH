#ifndef _SIRIUS_METADATA_P4_
#define _SIRIUS_METADATA_P4_

#include "dash_headers.p4"

#define MAX_ENI 64
#define MAX_HA_SET 1

enum bit<32> dash_routing_actions_t {
    STATIC_ENCAP = (1 << 0),
    NAT = (1 << 1),
    NAT46 = (1 << 2),
    NAT64 = (1 << 3),
    NAT_PORT = (1 << 4)
};

// Pipeline stages:
enum bit<16> dash_pipeline_stage_t {
    INVALID = 0,

    // Inbound stages
    INBOUND_STAGE_START = 100,

    // Outbound stages
    OUTBOUND_STAGE_START = 200,
    OUTBOUND_ROUTING = 200, // OUTBOUND_STAGE_START
    OUTBOUND_MAPPING = 201,
    OUTBOUND_PRE_ROUTING_ACTION_APPLY = 280,

    // Common stages
    ROUTING_ACTION_APPLY = 300
};

enum bit<8> dash_eni_mac_override_type_t {
    NONE = 0,
    SRC_MAC = 1,
    DST_MAC = 2
};

enum bit<8> dash_eni_mac_type_t {
    SRC_MAC = 0,
    DST_MAC = 1
};

struct conntrack_data_t {
    bool allow_in;
    bool allow_out;
}

enum bit<16> dash_tunnel_dscp_mode_t {
    PRESERVE_MODEL = 0,
    PIPE_MODEL = 1
}

struct outbound_routing_group_data_t {
    bit<16> outbound_routing_group_id;
    bool disabled;
}

struct eni_data_t {
    bit<32> cps;
    bit<32> pps;
    bit<32> flows;
    bit<1>  admin_state;
    IPv6Address pl_sip;
    IPv6Address pl_sip_mask;
    IPv4Address pl_underlay_sip;
    bit<6> dscp;
    dash_tunnel_dscp_mode_t dscp_mode;
    outbound_routing_group_data_t outbound_routing_group_data;
}

struct meter_context_t {
    bit<32> meter_class_or;
    bit<32> meter_class_and;
    bit<16> meter_policy_id;
    IPv4ORv6Address meter_policy_lookup_ip;
}

// HA roles
enum bit<8> dash_ha_role_t {
    DEAD = 0,
    ACTIVE = 1,
    STANDBY = 2,
    STANDALONE = 3,
    SWITCHING_TO_ACTIVE = 4
};

// HA states
enum bit<8> dash_ha_state_t {
    DEAD = 0,
    // trying to connect to HA pair
    CONNECTING = 1,
    // bulk sync in progress
    CONNECTED = 2,
    // connection successful, bulk sync in progress
    INITIALIZING_TO_ACTIVE      = 3,
    // connection successful, bulk sync in progress
    INITIALIZING_TO_STANDBY     = 4,
    // ready to be in STANDALONE state, waiting for activation of admin role
    PENDING_STANDALONE_ACTIVATION  = 5,
    // ready to be in ACTIVE state, waiting for activation of admin role
    PENDING_ACTIVE_ACTIVATION      = 6,
    // ready to be in STANDBY state, waiting for activation of admin role
    PENDING_STANDBY_ACTIVATION     = 7,
    // activation done, fowarding traffic
    STANDALONE = 8,
    // activation done, fowarding traffic and syncing flows with HA pair
    ACTIVE = 9,
    // activation done, ready to fowarding traffic if pair fails
    STANDBY = 10,
    // going down for planned shutdown
    DESTROYING = 11,
    // gracefully transitioning from paired state to stand-alone
    SWITCHING_TO_STANDALONE = 12
};

// Flow state
enum bit<8> dash_flow_state_t {
    FLOW_MISS = 0,                  // Flow not created yet
    FLOW_CREATED = 1,               // Flow is created but not synched or waiting for ack
    FLOW_SYNCED = 2,                // Flow has been synched to its peer
    FLOW_PENDING_DELETE = 3,        // Flow is pending deletion, waiting for ack
    FLOW_PENDING_RESIMULATION = 4   // Flow is marked as pending resimulation
};

struct ha_data_t {
    // HA scope settings
    bit<16> ha_scope_id;
    bit<16> ha_set_id;
    dash_ha_role_t ha_role;

    // HA set settings
    bit<1> local_ip_is_v6;
    IPv4ORv6Address local_ip;
    bit<1> peer_ip_is_v6;
    IPv4ORv6Address peer_ip;
    bit<16> dp_channel_dst_port;
    bit<16> dp_channel_src_port_min;
    bit<16> dp_channel_src_port_max;

    // HA packet/flow state
    dash_flow_state_t flow_sync_state;
}

struct metadata_t {
    // Packet type
    dash_packet_source_t packet_source; // TODO: Parse packet source in parser.
    dash_packet_type_t packet_type; // TODO: Parse packet type in parser.

    // Lookup context
    dash_direction_t direction;
    dash_eni_mac_type_t eni_mac_type;
    dash_eni_mac_override_type_t eni_mac_override_type;
    EthernetAddress eni_addr;
    bit<16> vnet_id;
    bit<16> dst_vnet_id;
    bit<16> eni_id;
    eni_data_t eni_data;
    bit<16> inbound_vm_id;
    bit<8> appliance_id;
    bit<1> is_overlay_ip_v6;
    bit<1> is_lkup_dst_ip_v6;
    bit<8> ip_protocol;
    IPv4ORv6Address dst_ip_addr;
    IPv4ORv6Address src_ip_addr;
    IPv4ORv6Address lkup_dst_ip_addr;
    bit<16> src_l4_port;
    bit<16> dst_l4_port;
    bit<16> stage1_dash_acl_group_id;
    bit<16> stage2_dash_acl_group_id;
    bit<16> stage3_dash_acl_group_id;
    bit<16> stage4_dash_acl_group_id;
    bit<16> stage5_dash_acl_group_id;
    bit<16> tunnel_pointer;
    bool is_fast_path_icmp_flow_redirection_packet;
    bit<1> fast_path_icmp_flow_redirection_disabled;
    meter_context_t meter_context;

    // HA
    ha_data_t ha;

    // Flow data
    conntrack_data_t conntrack_data;
    flow_table_data_t flow_table;
    dash_flow_state_t flow_state;
    bit<16> bulk_get_session_id;
    bit<16> bulk_get_session_filter_id;
    bool flow_enabled;
    bool to_dpapp;

    // Stage transition control
    dash_pipeline_stage_t target_stage;

    // Actions
    bit<32> routing_actions;

    // Action data
    bool dropped;
    // encap_data is for underlay
    encap_data_t encap_data;
    // tunnel_data is used by dash_tunnel_id
    encap_data_t tunnel_data;
    overlay_rewrite_data_t overlay_data;
    bit<16> dash_tunnel_id;
    bit<32> meter_class;
    bit<8> local_region_id;
}

#endif /* _SIRIUS_METADATA_P4_ */
