{ lib, buildPythonPackage
, django_2_2, psycopg2
}:

buildPythonPackage {
  pname = "dheck";
  version = "0.1";

  propagatedBuildInputs = [
    django_2_2
    psycopg2
  ];

  src = lib.cleanSource ./.;

  doCheck = false;
}
