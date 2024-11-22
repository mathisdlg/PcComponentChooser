{ pkgs ? import <nixpkgs> {} }:
let 
    pythonModules = with pkgs.python312Packages; [
        pip
        django
        django-bootstrap5
        django-debug-toolbar
        mysqlclient
    ];
in pkgs.mkShellNoCC {
    packages = with pkgs;[
        python312
    ] ++ pythonModules;

    LANG = "";
    LC_COLLATE = "C";
    LC_CTYPE = "UTF-8";
    LC_MESSAGES = "C";
    LC_MONETARY = "C";
    LC_NUMERIC = "C";
    LC_TIME = "C";

    shellHook = ''
        alias migrate='python manage.py makemigrations && python manage.py migrate'
        alias server='python manage.py runserver'
        python manage.py runserver
    '';
}