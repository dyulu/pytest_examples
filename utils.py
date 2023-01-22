import subprocess

def shell(cmd, timeout = 5):
    """ Run a shell command and return its output
        In case of any error or exception, print a message and fail it

        Python 3.11.1:
        Run the command described by args. Wait for command to complete, then return a CompletedProcess instance.
        subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False,
                       shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None,
                       text=None, env=None, universal_newlines=None, **other_popen_kwargs)
          New in 3.5: The recommended approach to invoking subprocesses is to use the run() function for all use
                      cases it can handle.
                      For more advanced use cases, the underlying Popen interface can be used directly.
          3.6: added encoding and errors parameters
          3.7: added parameter text as a more understandable alias of universal_newlines
               added parameter capture_output
          
    """

    try:
      # Pre-3.7
      # completedProcess = subprocess.run(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, check = True, timeout = timeout)
      completedProcess = subprocess.run(cmd, capture_output = True, text = True, check = True, timeout = timeout)
    except Exception as e:
        # Exceptions: 
        #   subprocess.TimeoutExpired:     process timed out
        #   subprocess.CalledProcessError: process did not return a successful return code (when setting check = True)
        #   FileNotFoundError:             executable could not be found
        print(f"Exception: {e}")
        raise

    return completedProcess.stdout.strip().split('\n')

def shell_w_popen(cmd, timeout = 5):
    """ Run a shell command and return its output
        In case of any error or exception, print a message and fail it

        Python 3.11.1:
        class subprocess.Popen(args, bufsize=- 1, executable=None, stdin=None, stdout=None, stderr=None,
                               preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None,
                               universal_newlines=None, startupinfo=None, creationflags=0, restore_signals=True,
                               start_new_session=False, pass_fds=(), *, group=None, extra_groups=None, user=None,
                               umask=- 1, encoding=None, errors=None, text=None, pipesize=- 1, process_group=None)
    """

    process = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    try:
        stdout, stderr = process.communicate(timeout = timeout)
    except subprocess.TimeoutExpired:
        process.kill()
        print('Exception: TimeoutExpired')
        stdout, stderr = process.communicate()
        print(f'{stdout}')
        print(f'{stderr}')
        raise
    except Exception as e:
        print("Exception: {}".format(e))
        raise

    if stderr:
        print(stderr.decode("utf-8"))
        raise Exception(stderr.decode("utf-8"))

    return stdout.decode('utf8').strip().split('\n')
