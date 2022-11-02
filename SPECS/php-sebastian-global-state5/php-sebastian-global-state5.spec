# spec file for php-sebastian-global-state4
#
# Copyright (c) 2014-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# Namespace
%global php_home     %{_datadir}/php

Name:           php-sebastian-global-state5
Version:        5.0.5
Release:        2%{?dist}
Summary:        Snapshotting of global state, version 5

License:        BSD
URL:            https://github.com/sebastianbergmann/global-state
Source0:        https://github.com/sebastianbergmann/global-state/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-reflection
BuildRequires:  php-spl
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
BuildRequires:  (php-composer(sebastian/object-reflector)  >= 2.0     with php-composer(sebastian/object-reflector)  < 3)
BuildRequires:  (php-composer(sebastian/recursion-context) >= 4.0     with php-composer(sebastian/recursion-context) < 5)
# from composer.json, "require-dev": {
#        "ext-dom": "*",
#        "phpunit/phpunit": "^9.3"
BuildRequires:  phpunit9 >= 9.3
BuildRequires:  php-dom
%endif

# from composer.json, "require": {
#        "php": ">=7.3",
#        "sebastian/object-reflector": "^2.0",
#        "sebastian/recursion-context": "^4.0"
Requires:       php(language) >= 7.3
Requires:       (php-composer(sebastian/object-reflector)  >= 2.0     with php-composer(sebastian/object-reflector)  < 3)
Requires:       (php-composer(sebastian/recursion-context) >= 4.0     with php-composer(sebastian/recursion-context) < 5)
# from phpcompatinfo report for version 4.0.0
Requires:       php-reflection
Requires:       php-spl
# from composer.json, "suggest": {
#        "ext-uopz": "*"
%if 0%{?fedora} > 21 || 0%{?rhel} >= 8
Suggests:       php-uopz
%endif
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sebastian/global-state) = %{version}


%description
Snapshotting of global state,
factored out of PHPUnit into a stand-alone component.


%prep
%setup -q 


%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/SebastianBergmann/ObjectReflector2/autoload.php',
    '%{php_home}/SebastianBergmann/RecursionContext4/autoload.php',
]);
EOF

# For the test suite
phpab --template fedora --output tests/autoload.php tests/_fixture/


%install
mkdir -p   %{buildroot}%{php_home}/SebastianBergmann
cp -pr src %{buildroot}%{php_home}/SebastianBergmann/GlobalState5


%check
%if %{with tests}
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require_once 'tests/autoload.php';
require_once 'tests/_fixture/SnapshotFunctions.php';
EOF

# testInterfaces and testConstructorExcludesAspectsWhenTheyShouldNotBeIncluded
# mays fails locally with psr extension
# testCanExportGlobalVariablesToCode, testStaticNotInitialisedAttributes temporarily fails (use old version ?)

: Run upstream test suite
ret=0
for cmd in php php74 php80 php81; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/SebastianBergmann/GlobalState5/autoload.php \
     %{_bindir}/phpunit9 \
       --filter '^((?!(testConstructorExcludesAspectsWhenTheyShouldNotBeIncluded|testCanExportGlobalVariablesToCode|testStaticNotInitialisedAttributes)).)*$' \
       --verbose || ret=1
  fi
done
exit $ret

%else
: bootstrap build with test suite disabled
%endif


%files
%license LICENSE
%doc README.md
%doc composer.json
%{php_home}/SebastianBergmann/GlobalState5


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 14 2022 Remi Collet <remi@remirepo.net> - 5.0.5-1
- update to 5.0.5

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 14 2021 Remi Collet <remi@remirepo.net> - 5.0.3-1
- update to 5.0.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Remi Collet <remi@remirepo.net> - 5.0.2-1
- update to 5.0.2

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 5.0.1-1
- update to 5.0.1 (no change)

* Fri Aug 28 2020 Remi Collet <remi@remirepo.net> - 5.0.0-2
- enable test suite

* Mon Aug 10 2020 Remi Collet <remi@remirepo.net> - 5.0.0-1
- update to 5.0.0
- rename to php-sebastian-global-state5
- move to /usr/share/php/SebastianBergmann/GlobalState5

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 4.0.0-1
- update to 4.0.0
- raise dependency on PHP 7.3
- raise dependency on sebastian/object-reflector 2
- raise dependency on sebastian/recursion-context 4
- rename to php-sebastian-global-state4
- move to /usr/share/php/SebastianBergmann/GlobalState4

* Fri Feb 22 2019 Remi Collet <remi@remirepo.net> - 3.0.0-2
- normal build

* Tue Feb 12 2019 Remi Collet <remi@remirepo.net> - 3.0.0-0.1
- fix directory ownership, from review #1671662

* Fri Feb  1 2019 Remi Collet <remi@remirepo.net> - 3.0.0-0
- boostrap build
- rename to php-sebastian-global-state3
- update to 3.0.0
- raise dependency on PHP 7.2
- add dependency on sebastian/object-reflector
- add dependency on sebastian/recursion-context

* Fri Apr 28 2017 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- rename to php-sebastian-global-state2
- update to 2.0.0
- raise dependency on PHP 7.0

* Fri Oct 21 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-4
- switch to fedora/autoloader

* Thu Oct 13 2016 Remi Collet <remi@fedoraproject.org> - 1.1.1-3
- add optional dependency on uopz extension

* Mon Oct 12 2015 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1

* Fri Dec  5 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package
