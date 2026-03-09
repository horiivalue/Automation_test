import json

with open("sample.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data["PDF"]["Sharoshi1"])
print(data["URL"]["Google"])


def update_json_value(data, keys, new_value):
    """
    keys: ["PDF", "Sharoshi1"] のように階層をリストで渡す
    """
    d = data
    for k in keys[:-1]:
        if k not in d:
            raise KeyError(f"キーが存在しません: {k}")
        d = d[k]

    last_key = keys[-1]
    if last_key not in d:
        raise KeyError(f"キーが存在しません: {last_key}")

    d[last_key] = new_value

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

update_json_value(data, ["PDF", "Sharoshi1"], "updated_path.pdf")
update_json_value(data, ["URL", "Homepage"], "https://newsite.com")

print(data["PDF"]["Sharoshi1"])
print(data["URL"]["Google"])

save_json("sample2.json", data)
save_json("sample2.json", data)
