import boto3
import ipaddress


def check_ip_in_ranges(ip, ranges, exclude_ranges):
    """Check if an IP is within a list of ranges and not in the exclude ranges."""
    for range in ranges:
        if ipaddress.ip_network(ip).subnet_of(ipaddress.ip_network(range)):
            for exclude_range in exclude_ranges:
                if ipaddress.ip_network(ip).subnet_of(ipaddress.ip_network(exclude_range)):
                    return False
            return True
    return False


def check_security_groups(region):
    """Check security groups for certain IP ranges."""
    ec2 = boto3.resource('ec2', region_name=region)

    ranges_to_check = ['172.0.0.0/8']
    exclude_ranges = ['172.16.0.0/12']

    for group in ec2.security_groups.all():
        for rule in group.ip_permissions:
            for ip_range in rule.get('IpRanges', []):
                if check_ip_in_ranges(ip_range.get('CidrIp', ''), ranges_to_check, exclude_ranges):
                    print(f"Security Group {group.group_name} ({group.group_id}) "
                          f"has an inbound rule that allows traffic from '{ip_range['CidrIp']}'")


def main():
    region = input('Enter the region to search in: ')
    check_security_groups(region)


if __name__ == "__main__":
    main()
