import pexpect
import sys
from sys import platform

if __name__ == '__main__':
    apkName = sys.argv[1]
    if sys.platform == "win32":
        import wexpect

        child = wexpect.spawn('androguard analyze')
        child.expect(']:')
        child.sendline(f"a, d, dx = AnalyzeAPK('./media/apks/{apkName}')")
        child.expect('2]: ', timeout=None)
        child.sendline("a.get_app_name()")

        child.expect('3]: ', timeout=None)
        child.sendline("a.get_permissions()")
        name = child.before.split("Out[2]:")[1].split("In [")[0].strip()

        child.expect('4]: ', timeout=None)
        child.sendline("a.get_activities()")
        permissions = child.before.split("Out[3]:")[1].split("In [")[0].strip()

        child.expect('5]: ', timeout=None)
        child.sendline("a.get_signature()")
        activities = child.before.split("Out[4]:")[1].split("In [")[0].strip()

        child.expect('6]: ', timeout=None)
        child.sendline("a.get_signature_name()")
        signature = child.before.split("Out[5]:")[1].split("In [")[0].strip()

        child.expect('7]: ', timeout=None)
        signature_name = child.before.split("Out[6]:")[1].split("In [")[0].strip()
    else:
        child = pexpect.spawn("androguard analyze", encoding='utf-8')
        child.expect(']: ', timeout=None)
        child.sendline(f"a, d, dx = AnalyzeAPK('./media/apks/{apkName}.apk')")
        child.expect(']: ', timeout=None)

        child.sendline("a.get_app_name()")
        child.expect(']: ', timeout=None)
        child.expect(']: ', timeout=None)
        child.expect(']: ', timeout=None)
        child.expect(']: ', timeout=None)

        child.sendline("a.get_permissions()")
        name = child.before.split("In [")[0].strip()
        child.expect(']: ', timeout=None)
        child.expect(']: ', timeout=None)
        child.expect(']: ', timeout=None)

        child.sendline("a.get_activities()")
        permissions = child.before.split("In [")[0].strip()
        child.expect(']: ', timeout=None)
        child.expect(']: ', timeout=None)
        child.expect(']: ', timeout=None)

        child.sendline("a.get_signature()")
        activities = child.before.split("In [")[0].strip()
        child.expect(']: ', timeout=None)
        child.expect(']: ', timeout=None)
        child.expect(']: ', timeout=None)

        child.sendline("a.get_signature_name()")
        signature = child.before.split("In [")[0].strip()
        child.expect(']: ', timeout=None)
        child.expect(']: ', timeout=None)
        child.expect(']: ', timeout=None)

        signature_name = child.before.split("In [")[0].strip()
    print(name, "breakAttribute", permissions, "breakAttribute", activities, "breakAttribute", signature,
          "breakAttribute", signature_name)
    child.sendline('exit')
    child.wait()
