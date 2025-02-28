#ifndef _DASH_ROUTING_ACTION_NAT46_P4_
#define _DASH_ROUTING_ACTION_NAT46_P4_

action push_action_nat46(
    in headers_t hdr,
    inout metadata_t meta,
    in IPv6Address sip,
    in IPv6Address sip_mask,
    in IPv6Address dip,
    in IPv6Address dip_mask)
{
    meta.routing_actions = meta.routing_actions | dash_routing_actions_t.NAT46;
    
    meta.overlay_data.is_ipv6 = 1;
    meta.overlay_data.sip = sip;
    meta.overlay_data.sip_mask = sip_mask;
    meta.overlay_data.dip = dip;
    meta.overlay_data.dip_mask = dip_mask;
}

control do_action_nat46(
    inout headers_t hdr,
    in metadata_t meta)
{
    apply {
        if (meta.routing_actions & dash_routing_actions_t.NAT46 == 0) {
            return;
        }

        REQUIRES(meta.overlay_data.is_ipv6 == 1);

        hdr.u0_ipv6.setValid();
        hdr.u0_ipv6.version = 6;
        hdr.u0_ipv6.traffic_class = 0;
        hdr.u0_ipv6.flow_label = 0;
        hdr.u0_ipv6.payload_length = hdr.u0_ipv4.total_len - IPV4_HDR_SIZE;
        hdr.u0_ipv6.next_header = hdr.u0_ipv4.protocol;
        hdr.u0_ipv6.hop_limit = hdr.u0_ipv4.ttl;
#ifndef DISABLE_128BIT_ARITHMETIC
        // As of 2024-Feb-09, p4c-dpdk does not yet support arithmetic on
        // 128-bit operands.
        hdr.u0_ipv6.dst_addr = ((IPv6Address)hdr.u0_ipv4.dst_addr & ~meta.overlay_data.dip_mask) | (meta.overlay_data.dip & meta.overlay_data.dip_mask);
        hdr.u0_ipv6.src_addr = ((IPv6Address)hdr.u0_ipv4.src_addr & ~meta.overlay_data.sip_mask) | (meta.overlay_data.sip & meta.overlay_data.sip_mask);
#endif
        
        hdr.u0_ipv4.setInvalid();
        hdr.u0_ethernet.ether_type = IPV6_ETHTYPE;
    }
}

#endif /* _DASH_ROUTING_ACTION_NAT46_P4_ */
