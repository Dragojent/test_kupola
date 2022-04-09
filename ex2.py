def extract_numbers(string):
    value = []
    for word in string.split():
        try: value.append(int(word))
        except: pass
        
    return value
        

def main():
    a = "1asd 12 sdf1 34 gf 567 fd 8 9"
    print(extract_numbers(a))


if __name__ == '__main__':
    main()