import dns.resolver

def get_members(domain, record_type = 'NS'):
    answers = []

    domain_servers = dns.resolver.resolve(domain, record_type)
    for resp in domain_servers:
        if record_type == 'NS':
            answers += get_members(resp.target, 'A')
        else:
            answers.append(resp.address)

    print(answers)

    return answers