def identificar_categoria_gadget(codigo):
    if codigo.startswith("T"):
        return "tablet"
    if codigo.startswith("P"):
        return "phone"
    if codigo.startswith("N"):
        return "notebook"
    return "unknown"

codigo_gadget = input().strip()
categoria = identificar_categoria_gadget(codigo_gadget)
print(categoria)
