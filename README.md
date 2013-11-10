# Credits

- smartgrid (discovery=mmisc, script=mmisc)
- railway (discovery=mmisc, script=schinken, patch=mmisc)
- bank (discovery=mmisc, script=schinken, patch=(krisha,schinken))

- keysubmitter.py (script=schinken)

# Runner scripts & submission

Runner scripts executes exploits on all hosts and store it into a keyfile

All keyfiles are piped into our local keysubmitter server to deduplicate keys so we don't nag the keyserver.

  tail -n 300 -f keyfiles/* | nc localhost 8080

The keysubmitter outputs this:

  2013-11-09 23:25:49.454430 Submitted key (c49f6897d55e7ee1) from ('127.0.0.1', 45476) :: [Unknown flag.]
  2013-11-09 23:25:49.480109 Submitted key (802aa2ab0ef7541c) from ('127.0.0.1', 45476) :: [Flag validity expired.]
  2013-11-09 23:25:49.584813 Submitted key (6e1be0a35aeaec8e) from ('127.0.0.1', 45476) :: [Unknown flag.]
  2013-11-09 23:26:01.668624 Submitted key (1c872677083c0916) from ('127.0.0.1', 45476) :: [Flag validity expired.]
  2013-11-09 23:26:09.477799 Submitted key (91c31c3f0c37ff1f) from ('127.0.0.1', 45239) :: [Congratulations, you scored a point!]
  2013-11-09 23:26:10.210216 Submitted key (d2cb81e36f1a2c23) from ('127.0.0.1', 45239) :: [Congratulations, you scored a point!]
  2013-11-09 23:26:11.125783 Submitted key (05ba001da35ab6fd) from ('127.0.0.1', 45239) :: [Congratulations, you scored a point!]
  2013-11-09 23:26:11.225214 Submitted key (f1947e6a79e43dbb) from ('127.0.0.1', 45239) :: [Congratulations, you scored a point!]
  2013-11-09 23:26:11.402758 Submitted key (694d11948c3822ed) from ('127.0.0.1', 45239) :: [Congratulations, you scored a point!]
  2013-11-09 23:26:11.494490 Submitted key (c4cb9c1ef58a45ef) from ('127.0.0.1', 45239) :: [Congratulations, you scored a point!]
