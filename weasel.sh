#!/usr/bin/bash


####################################
# Name      : Weasel Framework
# Developer : iamramahibrah
####################################




info()
{
  clear
  echo
  echo -e "
  [+]  WEASEL FRAMEWORK 🔴


    \e[1;32m*********\e[0m
    Tool name : Weasel framework
    Warranty  : MIT
    Developer : iamramahibrah
    Purpose   : Vulnerability Scan & Security audit
    Since     : 2021 
    \e[1;32m*********\e[0m "
}
info

while [ $# -gt 0 ]; do
  case "$1" in
    --help)
      menu
      ;;

    *)
      >&2 printf "Error: Invalid argument\n"
      exit 1
      ;;
  esac
  shift
done

