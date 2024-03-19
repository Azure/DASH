###############################################################
#                  Declaring Global variables
###############################################################

TOTALPACKETS = 1000
BW = 100
PACKET_LENGTH = 128
ENI_IP = "1.1.0.1"
NETWORK_IP1 = "1.128.0.1"
NETWORK_IP2 = "1.128.0.3"

DPU_VTEP_IP = "221.0.0.2"
ENI_VTEP_IP = "221.0.1.11"
NETWORK_VTEP_IP = "221.0.2.101"

OUTER_SRC_MAC = "80:09:02:01:00:01"
OUTER_DST_MAC = "c8:2c:2b:00:d1:30" 
INNER_SRC_MAC = "00:1A:C5:00:00:01"
INNER_DST_MAC = "00:1b:6e:00:00:01"
INNER_DST_MAC2= "00:1b:6e:00:00:03"
OUTER_SRC_MAC_F2 = "80:09:02:02:00:01"
OUTER_DST_MAC_F2 = "c8:2c:2b:00:d1:34"  

###############################################################
#                  DPU Config
###############################################################
dpu_config = [
  {
    "name": "vpe_#1",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_VIP_ENTRY",
    "key": {
      "switch_id": "$SWITCH_ID",
      "vip": DPU_VTEP_IP
    },
    "attributes": [
      "SAI_VIP_ENTRY_ATTR_ACTION", "SAI_VIP_ENTRY_ACTION_ACCEPT"
    ]
  },
  {
    "name": "dle_#1",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY",
    "key": {
      "switch_id": "$SWITCH_ID",
      "vni": "11"
    },
    "attributes": [
      "SAI_DIRECTION_LOOKUP_ENTRY_ATTR_ACTION", "SAI_DIRECTION_LOOKUP_ENTRY_ACTION_SET_OUTBOUND_DIRECTION"
    ]
  },
    {
    "name": "dle_#2",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_DIRECTION_LOOKUP_ENTRY",
    "key": {
      "switch_id": "$SWITCH_ID",
      "vni": "101"
    },
    "attributes": [
      "SAI_DIRECTION_LOOKUP_ENTRY_ATTR_ACTION", "SAI_DIRECTION_LOOKUP_ENTRY_ACTION_SET_OUTBOUND_DIRECTION"
    ]
  },

  {
    "name": "in_acl_group_id",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_DASH_ACL_GROUP",
    "attributes": [
      "SAI_DASH_ACL_GROUP_ATTR_IP_ADDR_FAMILY", "SAI_IP_ADDR_FAMILY_IPV4"
    ]
  },
  {
    "name": "out_acl_group_id",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_DASH_ACL_GROUP",
    "attributes": [
      "SAI_DASH_ACL_GROUP_ATTR_IP_ADDR_FAMILY", "SAI_IP_ADDR_FAMILY_IPV4"
    ]
  },
  {
    "name": "vnet",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_VNET",
    "attributes": [
      "SAI_VNET_ATTR_VNI", "1000"
    ]
  },
  {
    "name": "eni_#1",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_ENI",
    "attributes": [
      "SAI_ENI_ATTR_CPS", "10000",
      "SAI_ENI_ATTR_BW", "100000",
      "SAI_ENI_ATTR_FLOWS", "100000",
      "SAI_ENI_ATTR_ADMIN_STATE", "True",
      "SAI_ENI_ATTR_VM_UNDERLAY_DIP", ENI_VTEP_IP,
      "SAI_ENI_ATTR_VM_VNI", "9",
      "SAI_ENI_ATTR_VNET_ID", "$vnet",
      "SAI_ENI_ATTR_PL_SIP", "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
      "SAI_ENI_ATTR_PL_SIP_MASK", "2001:0db8:85a3:0000:0000:0000:0000:0000",
      "SAI_ENI_ATTR_PL_UNDERLAY_SIP", "10.0.0.18",
      "SAI_ENI_ATTR_INBOUND_V4_STAGE1_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V4_STAGE2_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V4_STAGE3_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V4_STAGE4_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V4_STAGE5_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V6_STAGE1_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V6_STAGE2_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V6_STAGE3_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V6_STAGE4_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V6_STAGE5_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V4_STAGE1_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V4_STAGE2_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V4_STAGE3_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V4_STAGE4_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V4_STAGE5_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V6_STAGE1_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V6_STAGE2_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V6_STAGE3_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V6_STAGE4_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V6_STAGE5_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_V4_METER_POLICY_ID", "0",
      "SAI_ENI_ATTR_V6_METER_POLICY_ID", "0",
      "SAI_ENI_ATTR_DASH_TUNNEL_DSCP_MODE", "SAI_DASH_TUNNEL_DSCP_MODE_PRESERVE_MODEL",
      "SAI_ENI_ATTR_DSCP", "0",
      "SAI_ENI_ATTR_DISABLE_FAST_PATH_ICMP_FLOW_REDIRECTION", "False"
    ]
  },
    {
    "name": "eni_#2",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_ENI",
    "attributes": [
      "SAI_ENI_ATTR_CPS", "10000",
      "SAI_ENI_ATTR_BW", "100000",
      "SAI_ENI_ATTR_FLOWS", "100000",
      "SAI_ENI_ATTR_ADMIN_STATE", "True",
      "SAI_ENI_ATTR_VM_UNDERLAY_DIP", NETWORK_VTEP_IP,
      "SAI_ENI_ATTR_VM_VNI", "9",
      "SAI_ENI_ATTR_VNET_ID", "$vnet",
      "SAI_ENI_ATTR_PL_SIP", "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
      "SAI_ENI_ATTR_PL_SIP_MASK", "2001:0db8:85a3:0000:0000:0000:0000:0000",
      "SAI_ENI_ATTR_PL_UNDERLAY_SIP", "10.0.0.18",
      "SAI_ENI_ATTR_INBOUND_V4_STAGE1_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V4_STAGE2_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V4_STAGE3_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V4_STAGE4_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V4_STAGE5_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V6_STAGE1_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V6_STAGE2_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V6_STAGE3_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V6_STAGE4_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V6_STAGE5_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V4_STAGE1_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V4_STAGE2_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V4_STAGE3_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V4_STAGE4_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V4_STAGE5_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V6_STAGE1_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V6_STAGE2_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V6_STAGE3_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V6_STAGE4_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V6_STAGE5_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_V4_METER_POLICY_ID", "0",
      "SAI_ENI_ATTR_V6_METER_POLICY_ID", "0",
      "SAI_ENI_ATTR_DASH_TUNNEL_DSCP_MODE", "SAI_DASH_TUNNEL_DSCP_MODE_PRESERVE_MODEL",
      "SAI_ENI_ATTR_DSCP", "0",
      "SAI_ENI_ATTR_DISABLE_FAST_PATH_ICMP_FLOW_REDIRECTION", "False"
    ]
  },
  {
    "name": "eni_#3",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_ENI",
    "attributes": [
      "SAI_ENI_ATTR_CPS", "10000",
      "SAI_ENI_ATTR_BW", "100000",
      "SAI_ENI_ATTR_FLOWS", "100000",
      "SAI_ENI_ATTR_ADMIN_STATE", "True",
      "SAI_ENI_ATTR_VM_UNDERLAY_DIP", NETWORK_VTEP_IP,
      "SAI_ENI_ATTR_VM_VNI", "9",
      "SAI_ENI_ATTR_VNET_ID", "$vnet",
      "SAI_ENI_ATTR_PL_SIP", "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
      "SAI_ENI_ATTR_PL_SIP_MASK", "2001:0db8:85a3:0000:0000:0000:0000:0000",
      "SAI_ENI_ATTR_PL_UNDERLAY_SIP", "10.0.0.18",
      "SAI_ENI_ATTR_INBOUND_V4_STAGE1_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V4_STAGE2_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V4_STAGE3_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V4_STAGE4_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V4_STAGE5_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V6_STAGE1_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V6_STAGE2_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V6_STAGE3_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V6_STAGE4_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_INBOUND_V6_STAGE5_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V4_STAGE1_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V4_STAGE2_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V4_STAGE3_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V4_STAGE4_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V4_STAGE5_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V6_STAGE1_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V6_STAGE2_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V6_STAGE3_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V6_STAGE4_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_OUTBOUND_V6_STAGE5_DASH_ACL_GROUP_ID", "0",
      "SAI_ENI_ATTR_V4_METER_POLICY_ID", "0",
      "SAI_ENI_ATTR_V6_METER_POLICY_ID", "0",
      "SAI_ENI_ATTR_DASH_TUNNEL_DSCP_MODE", "SAI_DASH_TUNNEL_DSCP_MODE_PRESERVE_MODEL",
      "SAI_ENI_ATTR_DSCP", "0",
      "SAI_ENI_ATTR_DISABLE_FAST_PATH_ICMP_FLOW_REDIRECTION", "False"
    ]
  },

  {
    "name": "eam",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY",
    "key": {
      "switch_id": "$SWITCH_ID",
      "address": INNER_SRC_MAC
    },
    "attributes": [
      "SAI_ENI_ETHER_ADDRESS_MAP_ENTRY_ATTR_ENI_ID", "$eni_#1"
    ]
  },
  {
    "name": "eam2",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY",
    "key": {
      "switch_id": "$SWITCH_ID",
      "address": INNER_DST_MAC
    },
    "attributes": [
      "SAI_ENI_ETHER_ADDRESS_MAP_ENTRY_ATTR_ENI_ID", "$eni_#2"
    ]
  },
  {
    "name": "eam3",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY",
    "key": {
      "switch_id": "$SWITCH_ID",
      "address": INNER_DST_MAC2
    },
    "attributes": [
      "SAI_ENI_ETHER_ADDRESS_MAP_ENTRY_ATTR_ENI_ID", "$eni_#3"
    ]
  },
  {
    "name": "ore",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY",
    "key": {
      "switch_id": "$SWITCH_ID",
      "eni_id": "$eni_#1",
      "destination": "1.0.0.0/8"
    },
    "attributes": [
      "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_ACTION", "SAI_OUTBOUND_ROUTING_ENTRY_ACTION_ROUTE_VNET",
      "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DST_VNET_ID", "$vnet",
      "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_METER_POLICY_EN", "False",
      "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_METER_CLASS", "0"
    ]
  },
    {
    "name": "ore2",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY",
    "key": {
      "switch_id": "$SWITCH_ID",
      "eni_id": "$eni_#2",
      "destination": "1.0.0.0/8"
    },
    "attributes": [
      "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_ACTION", "SAI_OUTBOUND_ROUTING_ENTRY_ACTION_ROUTE_VNET",
      "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DST_VNET_ID", "$vnet",
      "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_METER_POLICY_EN", "False",
      "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_METER_CLASS", "0"
    ]
  },
  {
    "name": "ore3",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY",
    "key": {
      "switch_id": "$SWITCH_ID",
      "eni_id": "$eni_#3",
      "destination": "1.0.0.0/8"
    },
    "attributes": [
      "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_ACTION", "SAI_OUTBOUND_ROUTING_ENTRY_ACTION_ROUTE_VNET",
      "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_DST_VNET_ID", "$vnet",
      "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_METER_POLICY_EN", "False",
      "SAI_OUTBOUND_ROUTING_ENTRY_ATTR_METER_CLASS", "0"
    ]
  },
    {
    "name": "inbound_routing_entry",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY",
    "key": {
      "switch_id": "$SWITCH_ID",
      "eni_id": "$eni_#1",
      "vni": "11",
      "sip": "1.1.0.0",
      "sip_mask": "255.255.255.0",
      "priority": 0
    },
    "attributes": [
      "SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION",
      "SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP_PA_VALIDATE",
      "SAI_INBOUND_ROUTING_ENTRY_ATTR_SRC_VNET_ID",
      "$vnet"
    ]
  },
    {
    "name": "inbound_routing_entry2",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY",
    "key": {
      "switch_id": "$SWITCH_ID",
      "eni_id": "$eni_#2",
      "vni": "101",
      "sip": "1.128.0.0",
      "sip_mask": "255.255.255.0",
      "priority": 0
    },
    "attributes": [
      "SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION",
      "SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP_PA_VALIDATE",
      "SAI_INBOUND_ROUTING_ENTRY_ATTR_SRC_VNET_ID",
      "$vnet"
    ]
  },
  {
    "name": "inbound_routing_entry3",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_INBOUND_ROUTING_ENTRY",
    "key": {
      "switch_id": "$SWITCH_ID",
      "eni_id": "$eni_#3",
      "vni": "101",
      "sip": "1.128.0.0",
      "sip_mask": "255.255.255.0",
      "priority": 0
    },
    "attributes": [
      "SAI_INBOUND_ROUTING_ENTRY_ATTR_ACTION",
      "SAI_INBOUND_ROUTING_ENTRY_ACTION_VXLAN_DECAP_PA_VALIDATE",
      "SAI_INBOUND_ROUTING_ENTRY_ATTR_SRC_VNET_ID",
      "$vnet"
    ]
  },
  {
    "name": "ocpe",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY",
    "key": {
      "switch_id": "$SWITCH_ID",
      "dst_vnet_id": "$vnet",
      "dip": NETWORK_IP1
    },
    "attributes": [
      "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_UNDERLAY_DIP", NETWORK_VTEP_IP,
      "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_OVERLAY_DMAC", INNER_DST_MAC,
      "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_USE_DST_VNET_VNI", "True",
      "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_METER_CLASS", "0",
      "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_METER_CLASS_OVERRIDE", "False"
    ]
  },
  {
    "name": "ocpe1",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY",
    "key": {
      "switch_id": "$SWITCH_ID",
      "dst_vnet_id": "$vnet",
      "dip": NETWORK_IP2
    },
    "attributes": [
      "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_UNDERLAY_DIP", NETWORK_VTEP_IP,
      "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_OVERLAY_DMAC", INNER_DST_MAC2,
      "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_USE_DST_VNET_VNI", "True",
      "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_METER_CLASS", "0",
      "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_METER_CLASS_OVERRIDE", "False"
    ]
  },
    {
    "name": "ocpe2",
    "op": "create",
    "type": "SAI_OBJECT_TYPE_OUTBOUND_CA_TO_PA_ENTRY",
    "key": {
      "switch_id": "$SWITCH_ID",
      "dst_vnet_id": "$vnet",
      "dip": ENI_IP
    },
    "attributes": [
      "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_UNDERLAY_DIP", ENI_VTEP_IP,
      "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_OVERLAY_DMAC", INNER_SRC_MAC,
      "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_USE_DST_VNET_VNI", "True",
      "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_METER_CLASS", "0",
      "SAI_OUTBOUND_CA_TO_PA_ENTRY_ATTR_METER_CLASS_OVERRIDE", "False"
    ]
  }
]

