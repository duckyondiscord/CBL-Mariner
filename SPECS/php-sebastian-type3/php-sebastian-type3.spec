# remirepo/fedora spec file for php-sebastian-type3
#
# Copyright (c) 2019-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# namespace
%global php_home     %{_datadir}/php

Name:           php-sebastian-type3
Version:        3.2.0
Release:        1%{?dist}
Summary:        Collection of value objects that represent the types of the PHP type system, v3

License:        BSD
URL:            https://github.com/sebastianbergmann/type
Source0:        https://github.com/sebastianbergmann/type/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-reflection
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.5"
BuildRequires:  phpunit9 >= 9.5
%endif

# from composer.json, "require": {
#        "php": ">=7.3",
Requires:       php(language) >= 7.3
# from phpcompatinfo report for version 1.0.0
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sebastian/type) = %{version}


%description
Collection of value objects that represent the types of the PHP type system.

This package provides version 3 of sebastian/type library.


%prep
%setup -q 


%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src

# For the test suite
phpab --template fedora --output tests/autoload.php tests/_fixture/


%install
mkdir -p   %{buildroot}%{php_home}/SebastianBergmann
cp -pr src %{buildroot}%{php_home}/SebastianBergmann/Type3


%check
%if %{with tests}
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require_once 'tests/autoload.php';
require_once 'tests/_fixture/callback_function.php';
require_once 'tests/_fixture/functions_that_declare_return_types.php';
EOF

: Run upstream test suite
ret=0
for cmd in php php74 php80 php81 php82; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/SebastianBergmann/Type3/autoload.php \
     %{_bindir}/phpunit9 \
       --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}/SebastianBergmann
     %{php_home}/SebastianBergmann/Type3


%changelog
* Tue Sep 13 2022 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0

* Tue Aug 30 2022 Remi Collet <remi@remirepo.net> - 3.1.0-1
- update to 3.1.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 27 2022 Remi Collet <remi@remirepo.net> - 3.0.0-2
- improve package description and summary

* Tue Mar 15 2022 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- rename to php-sebastian-type3
- install to /usr/share/php/SebastianBergmann/Type3

* Tue Jun 15 2021 Remi Collet <remi@remirepo.net> - 2.3.4-1
- update to 2.3.4

* Fri Jun  4 2021 Remi Collet <remi@remirepo.net> - 2.3.2-1
- update to 2.3.2

* Mon Oct 26 2020 Remi Collet <remi@remirepo.net> - 2.3.1-1
- update to 2.3.1

* Tue Oct  6 2020 Remi Collet <remi@remirepo.net> - 2.3.0-1
- update to 2.3.0

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 2.2.2-1
- update to 2.2.2 (no change)

* Mon Jul  6 2020 Remi Collet <remi@remirepo.net> - 2.2.1-1
- update to 2.2.1

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 2.1.1-1
- update to 2.1.1

* Tue Jun  2 2020 Remi Collet <remi@remirepo.net> - 2.1.0-1
- update to 2.1.0
- sources from git snapshot
- switch to phpunit9

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- raise dependency on PHP 7.3
- rename to php-sebastian-type2
- move to /usr/share/php/SebastianBergmann/Type2

* Tue Jul  2 2019 Remi Collet <remi@remirepo.net> - 1.1.3-1
- update to 1.1.3

* Wed Jun 19 2019 Remi Collet <remi@remirepo.net> - 1.1.2-1
- update to 1.1.2

* Sat Jun  8 2019 Remi Collet <remi@remirepo.net> - 1.1.1-1
- update to 1.1.1

* Sat Jun  8 2019 Remi Collet <remi@remirepo.net> - 1.1.0-1
- update to 1.1.0

* Fri Jun  7 2019 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package
