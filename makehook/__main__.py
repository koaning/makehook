import subprocess

def main():
    print(subprocess.check_output(['make check']))

if __name__ == "__main__":
    main()
