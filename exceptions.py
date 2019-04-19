
def div2Numbers(n1, n2):
    result = 0
    try:
        result = n1 / n2
    except ZeroDivisionError:
        print("hey you can't divide by 0")
        # use 'pass' to just do nothing
    #except:  <<catches all errors
    #finally:
        #file.close()

    return result

def main():
    n1 = 10
    n2 = 0
    print(div2Numbers(n1, n2))



main()