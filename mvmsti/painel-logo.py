import base64, glob, os, re, shutil, sys, urllib.request
ADMIN = sys.argv[1]
ORIG = urllib.request.urlopen("https://raw.githubusercontent.com/lejianwen/rustdesk-api-web/master/src/assets/logo.png").read()
NEW = urllib.request.urlopen("https://raw.githubusercontent.com/suportemvmsti/rustdesk/mvmsti/flutter/assets/icon.png").read()
ICO = urllib.request.urlopen("https://raw.githubusercontent.com/suportemvmsti/rustdesk/mvmsti/res/icon.ico").read()
open(os.path.join(ADMIN, "mvmsti-logo.png"), "wb").write(NEW)
open(os.path.join(ADMIN, "favicon.ico"), "wb").write(ICO)
orig_uri = "data:image/png;base64," + base64.b64encode(ORIG).decode()
hits = 0
for f in glob.glob(os.path.join(ADMIN, "**", "*.*"), recursive=True):
    if not f.endswith((".js", ".css", ".html")):
        continue
    s = open(f, encoding="utf-8").read()
    if orig_uri in s:
        s = s.replace(orig_uri, "./mvmsti-logo.png"); hits += 1
        open(f, "w", encoding="utf-8").write(s)
for f in glob.glob(os.path.join(ADMIN, "assets", "logo*.png")):
    shutil.copy(os.path.join(ADMIN, "mvmsti-logo.png"), f); hits += 1
print("Arquivos alterados:", hits)
