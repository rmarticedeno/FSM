import dns.resolver

# answers = dns.resolver.resolve('uh.cu', 'NS')
# for rdata in answers:
#     value = dns.resolver.resolve(rdata.target, 'A')
#     for x in value:
#         print(x.address)

def get_members(domain, record_type = 'NS'):
    answers = []

    domain_servers = dns.resolver.resolve(domain, record_type)
    for resp in domain_servers:
        if record_type == 'NS':
            answers = answers.join(get_members(resp.target, 'A'))
        else:
            answers.append(resp.address)

    return answers