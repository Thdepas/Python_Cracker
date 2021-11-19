import sys
import string
import hashlib
import urllib.request
import urllib.response
import urllib.error
from utils import *


class Cracker:

    @staticmethod
    def hash_crack(md5, file, order, done_queue):
        try:
            found = False
            ofile = open(file, "r")
            if Order.ASCEND == order:
                content = reversed(list(ofile.readlines()))
            else:
                content = ofile.readlines()
            for mot in content:
                mot = mot.strip("\n").encode("utf8")
                hashmd5 = hashlib.md5(mot).hexdigest()
                if hashmd5 == md5:
                    print(Couleur.VERT + "[+]FOUND PASSWORD ヾ(＠^∇^＠)ノ : " +
                          str(mot) + "(" + hashmd5 + ")" + Couleur.FIN)
                    found = True
                    done_queue.put("FOUND")
            if not found:
                print(Couleur.ROUGE +
                      "[-] PASSWORD NOT FOUND ʕ ಡ ﹏ ಡ ʔ" + Couleur.FIN)
                done_queue.put("NOT FOUND")
                ofile.close()
        except FileNotFoundError:
            print(Couleur.ROUGE + "[-] ERROR : FILE NOT FOUND !" + Couleur.FIN)
            sys.exit(1)
        except Exception as err:
            print(Couleur.ROUGE + "[-] ERROR ಠ╭╮ಠ : " + str(err) + Couleur.FIN)
            sys.exit(2)

    @staticmethod
    def crack_incr(md5, length, currpass=[]):
        lettres = string.ascii_letters
        if length >= 1:
            if len(ses = lt.session()
ses.listen_on(6881, 6891)

params = {
    'save_path': '/home/becode/Documents/Torrent',
    'storage_mode': lt.storage_mode_t(2)
}

handle = lt.add_magnet_uri(ses, magnet, params)
ses.start_dht()

begin = time.time()
print(datetime.datetime.now())

print('Downloading Metadata ....')
while(not handle.has_metadata()):
    time.sleep(1)

print('Got Metadata, Starting Torrent Download')
print('Starting', handle.name())

while(handle.status().state != lt.torrent_status.seeding):
    s = handle.status()
    state_str = ['queued', 'checking', 'downloading metadata'
                    'downloading', 'finished', 'seeding', 'allocating']
    print('% .2f %% complete (down: %.1f kb/s up: %.1f kb/s peers: %d) %s' %
            (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
            s.num_peers, state_str[s.state]))

    time.sleep(5)

end = time.time()
print(handle.name(), "COMPLETED")
print("Elasped Time:", int((end-begin) // 60),
        "min: ", int((end - begin) % 60), 'sec : ')
print(datetime.datetime.now())
currpass) == 0:
                currpass = ['a' for _ in range(length)]
                Cracker.crack_incr(md5, length, currpass)
            else:
                for c in lettres:
                    currpass[length - 1] = c
                    currhash = hashlib.md5(
                        "".join(currpass).encode("utf8")).hexdigest()
                    print("[*] TESTING : " + "".join(currpass) +
                          "(" + currhash + ")")
                    if hashlib.md5("".join(currpass).encode("utf8")).hexdigest() == md5:
                        print(Couleur.VERT + "[+] PASSWORD FOUND ヾ(＠^∇^＠)ノ : " +
                              "".join(currpass) + Couleur.FIN)
                        sys.exit(0)
                    else:
                        Cracker.crack_incr(md5, length - 1, currpass)

    @staticmethod
    def crack_online(md5):
        try:
            req_headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.A.B.C Safari/525.13'
            }
            url = 'https://www.google.fr/search?hl=fr&q=' + md5
            request = urllib.request.Request(url, headers=req_headers)
            opener = urllib.request.build_opener()
            reponse = opener.open(request)
        except urllib.error.HTTPError as e:
            print("HTTP Error : " + e.code)
        except urllib.error.URLError as e:
            print("URL Error : " + e.reason)
        if "Aucun document" in str(reponse.read()):
            print(Couleur.ROUGE + "[-] HASH NOT FOUND BY GOOGLE" + Couleur.FIN)
        else:
            print(Couleur.VERT +
                  "[+] PASSWORD FOUND BY GOOGLE ヾ(＠^∇^＠)ノ : " + url + Couleur.FIN)

    @staticmethod
    def crack_smart(md5, pattern, _index=0):
        MAJ = string.ascii_uppercase
        DIGIT = string.digits
        MIN = string.ascii_lowercase

        if _index < len(pattern):
            if pattern[_index] in MAJ + DIGIT + MIN:
                Cracker.crack_smart(md5, pattern, _index + 1)
            if "^" == pattern[_index]:
                for c in MAJ:
                    p = pattern.replace("^", c, 1)
                    currhash = hashlib.md5(p.encode("utf8")).hexdigest()
                    if currhash == md5:
                        print(Couleur.VERT +
                              "[+] PASSWORD FOUND ヾ(＠^∇^＠)ノ : " + p + Couleur.FIN)
                        sys.exit(0)
                    Cracker.crack_smart(md5, p, _index + 1)

            if "*" == pattern[_index]:
                for c in MIN:
                    p = pattern.replace("*", c, 1)
                    currhash = hashlib.md5(p.encode("utf8")).hexdigest()
                    if currhash == md5:
                        print(Couleur.VERT +
                              "[+] PASSWORD FOUND ヾ(＠^∇^＠)ノ : " + p + Couleur.FIN)
                        sys.exit(0)
                    Cracker.crack_smart(md5, p, _index + 1)

            if "-" == pattern[_index]:
                for c in DIGIT:
                    p = pattern.replace("-", c, 1)
                    currhash = hashlib.md5(p.encode("utf8")).hexdigest()
                    if currhash == md5:
                        print(Couleur.VERT +
                              "[+] PASSWORD FOUND ヾ(＠^∇^＠)ノ : " + p + Couleur.FIN)
                        sys.exit(0)
                    Cracker.crack_smart(md5, p, _index + 1)
            else:
                return

    @staticmethod
    def work(work_queue, done_queue, md5, file, order):
        o = work_queue.get()
        o.hash_crack(md5, file, order, done_queue)
