import multiprocessing.pool
import subprocess
concurrent = 25

def ping(ip):
    proc = subprocess.Popen(f"ping -w 250 -n 2 10.0.0.{ip}", stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()

    print(f"Pinged 10.0.0.{ip}")
    return out.decode("utf-8")

def main():
    pool = multiprocessing.pool.ThreadPool(processes=concurrent)
    return_list = pool.map(ping, range(1, 256))
    pool.close()
    pool.join()

    for i in return_list:
        print(i)

if __name__ == "__main__":
    main()