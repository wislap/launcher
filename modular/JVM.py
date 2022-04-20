import os
import requests
import json
import os
class jvmbuilder(object):
    def path(self,MinecraftPath):
        if os.path.lexists(MinecraftPath+r'\assets') == True :
            assets = MinecraftPath+r'\assets'

    def version(self):

        version_manifest_json_response = open(os.getcwd()+'\manifest.json', 'r+')
        if version_manifest_json_response.read() == "":

            version_manifest_json_url = r"https://launchermeta.mojang.com/mc/game/version_manifest.json"
            version_manifest_json_requests = requests.get(version_manifest_json_url)
            version_manifest_json_response.write(str(version_manifest_json_requests.content))
            version_manifest_json_response.flush()
        version_manifest_json_response.close()
        version_manifest = json.load(open(os.getcwd()+'\manifest.json'))
        for r in version_manifest["versions"] :
            print(r)


    def jvm(self,MineccraftPath,MinecraftVersion,MaxMemory,MinMemory):
        jvm = "java -Dminecraft.client.jar=" +r".minecraft\versions\%s\%s.jar "%(MinecraftVersion,MinecraftVersion) \
        + "-XX:+UseG1GC " + "-XX:-UseAdaptiveSizePolicy " + "-XX:-OmitStackTraceInFastThrow "+ "Dos.name=Windows 10 -Dos.version=10.0 " \
        + "-Dminecraft.launcher.brand=锋电启动器 -Dminecraft.launcher.version=1.0.0" \
        + "-Xmx%sm "%(MaxMemory) + "-Xmn%sm "%(MinMemory)\
        + "-Djava.library.path=" +r"%s\versions\%s\natives"%(MineccraftPath,MinecraftVersion)

        print(jvm)

a = jvmbuilder()
#a.jvm(r"F:\mc\原版mc\.minecraft","1.16.5",4096,4096)
a.version()