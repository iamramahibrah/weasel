#!/usr/bin/bash


####################################
# Name      : Weasel Framework
# Developer : iamramahibrah
####################################




info()
{
  clear
  echo
  echo -e -n "
  [+]  WEASEL FRAMEWORK \e[1;32m ● \e[0m


    \e[1;32m*********\e[0m
    Tool name : Weasel framework
    Warranty  : MIT
    Developer : iamramahibrah
    Purpose   : Vulnerability Scan & Security audit
    Since     : 2021 
    Version   : 0.1

    usage  (options) -Help
    \e[1;32m*********\e[0m"
}
info

function help()
{
  echo -e "

      Options:

          --css-injection     |  Scan for CSS Injection Vulnerability"
}

function css()
{
  echo -e "

  [+] \e[33;1m CCS-INJECTION VULNERABILITY \e[0m
           Powered by Nmap
                      \e[1;32m****\e[0m"
  echo
  echo -e -n "   Enter \e[33;1mhost target\e[0m: "
  read host
ping -c1 -W1 -q $host &>/dev/null
status=$( echo $? )
if [[ $status == 0 ]] ; then
    echo -e " $host .... [\e[1;32m Connected\e[0m] "
    echo -e "$YELLOW scanning $host for CCS-INJECTION $NOCOLOR"
    sleep 1s
    nmap -p5432 --script ssl-ccs-injection $host
else
   echo -e " $host ....  [$RED Server Down $NOCOLOR] "
fi
}

while [ $# -gt 0 ]; do
  case "$1" in
    -Help)
      help
      ;;
    --css-injection)
      css
      ;;

    *)
      >&2 printf "Error: Invalid argument\n"
      exit 1
      ;;
  esac
  shift
done

