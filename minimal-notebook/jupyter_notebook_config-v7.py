import os

port = int(os.environ.get('JUPYTER_NOTEBOOK_PORT', '8080'))

c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = port
c.NotebookApp.open_browser = False
c.NotebookApp.quit_button = False

if os.environ.get('JUPYTERHUB_SERVICE_PREFIX'):
    c.NotebookApp.base_url = os.environ.get('JUPYTERHUB_SERVICE_PREFIX')

password = os.environ.get('JUPYTER_NOTEBOOK_PASSWORD')
if password:
    import jupyter_server.auth

    from jupyter_server.auth import passwd
    hashed_password = passwd(password)
    file = open("/opt/app-root/src/.jupyter/jupyter_notebook_config.json", "w+")
    hashed_password_mod = repr(hashed_password)
    file.write("{" + "\n" + "  \"NotebookApp\": {" + "\n" + "    \"password\": " + "\"" + hashed_password_mod + "\"" + "\n" + "  }" + "\n" + "}" )
    file.close

    c.ServerApp.password = hashed_password
    c.NotebookApp.password = hashed_password
    del password
    del os.environ['JUPYTER_NOTEBOOK_PASSWORD']

image_config_file = '/opt/app-root/src/.jupyter/jupyter_notebook_config.py'

if os.path.exists(image_config_file):
    with open(image_config_file) as fp:
        exec(compile(fp.read(), image_config_file, 'exec'), globals())
