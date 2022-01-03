import random

def get_random_source():
    m = str(random.randint(1,254))
    k = str(random.randint(1,254))
    s = str(random.randint(1,254))
    e = str(random.randint(1,254))
    c = "."
    src = m+c+k+c+s+c+e
    return src
def save_to_file():
    file = open("proxies.txt","a",encoding="utf-8")
    file.write(get_random_source())
    file.write("\n")
    file.close()

index = 0
while 1:
    try:
        save_to_file()
        print(f"\rSaving to file: {get_random_source()} ",end="")
        index += 1
    except KeyboardInterrupt:
        print("\nProgram terminated.")
        print(f"Total {index} proxies created.")
        quit()