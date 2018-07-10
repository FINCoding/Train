import ftplib

def putfile(file, site, dir, user=(), *, verbose=True):
    if verbose: print('Uploading', file)
    local = open(file, 'rb')
    remote = ftplib.FTP(site)
    remote.login(*user)
    remote.cwd(dir)
    remote.storbinary('STOR' + file, local, 1024)
    remote.quit()
    local.close()
    if verbose: print('Upload done.')

if __name__ == '__main__':
    site = '172.30.0.142'
    dir = '.'
    import sys, getpass
    pswd = getpass.getpass(site + ' PASS?')
    putfile('D:\\1.png', site, dir, user=('User2', pswd))
    # putfile(sys.argv[1], site, dir, user=('User', pswd))