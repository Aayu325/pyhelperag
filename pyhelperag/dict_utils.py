import json

def deep_merge_dicts(a, b):
    for k, v in b.items():
        if isinstance(v, dict) and k in a:
            deep_merge_dicts(a[k], v)
        else:
            a[k] = v
    return a

def pretty_print_json(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))
