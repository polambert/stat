
import libstat as stat

def run():
    ## Loop input until user quits
    ans = 0

    while True:
        cmd = input("c> ")

        if cmd == "q":
            break
        else:
            try:
                ans = eval(str(cmd).replace("ans", str(ans)))

                print(" " + str(ans))
            except Exception as e:
                print(" " + stat.Colors.fail + stat.Colors.bold + "Error!" + stat.Colors.end)
                print(" : " + stat.Colors.fail + str(e) + stat.Colors.end)

