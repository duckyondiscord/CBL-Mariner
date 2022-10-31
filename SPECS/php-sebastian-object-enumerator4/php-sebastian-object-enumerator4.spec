# remirepo/fedora spec file for php-sebastian-object-enumerator4
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# Namespace
%global php_home     %{_datadir}/php

Name:           php-sebastian-object-enumerator4
Version:        4.0.4
Release:        2
Summary:        Traverses array and object to enumerate all referenced objects, version 4

License:        BSD
URL:            https://github.com/sebastianbergmann/object-enumerator
Source0:        https://github.com/sebastianbergmann/object-enumerator/archive/refs/tags/%{version}.tar.gz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-fedora-autoloader-devel
%if %{with_check}
BuildRequires:  (php-composer(sebastian/object-reflector) >= 2.0   with php-composer(sebastian/object-reflector) < 3)
BuildRequires:  (php-composer(sebastian/recursion-context)   >= 4.0   with php-composer(sebastian/recursion-context)   < 5)
# From composer.json"require-dev": {
#        "phpunit/phpunit": "^9.3"
BuildRequires:  phpunit9 >= 9.3
%endif

# from composer.json
#        "php": ">=7.3",
#        "sebastian/object-reflector": "^2.0",
#        "sebastian/recursion-context": "^4.0"
Requires:       php(language) >= 7.3
Requires:       (php-composer(sebastian/object-reflector) >= 2.0   with php-composer(sebastian/object-reflector) < 3)
Requires:       (php-composer(sebastian/recursion-context)   >= 4.0   with php-composer(sebastian/recursion-context)   < 5)
# from phpcompatinfo report for version 4.0.0:
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sebastian/object-enumerator) = %{version}


%description
Traverses array structures and object graphs to enumerate all
referenced objects.

Autoloader: %{php_home}/SebastianBergmann/ObjectEnumerator4/autoload.php


%prep
%setup -q


%build
# Generate the Autoloader, from composer.json "autoload": {
#        "classmap": [
#            "src/"
%{_bindir}/phpab --template fedora --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/SebastianBergmann/ObjectReflector2/autoload.php',
    '%{php_home}/SebastianBergmann/RecursionContext4/autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{php_home}/SebastianBergmann
cp -pr src %{buildroot}%{php_home}/SebastianBergmann/ObjectEnumerator4


%check
%if %{with_check}
mkdir vendor
%{_bindir}/phpab --template fedora --output vendor/autoload.php tests/_fixture

: Run upstream test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/SebastianBergmann/ObjectEnumerator4/autoload.php \
     %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%license LICENSE
%doc README.md composer.json
%{php_home}/SebastianBergmann/ObjectEnumerator4


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-1.2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Remi Collet <remi@remirepo.net> - 4.0.4-1
- update to 4.0.4

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 4.0.3-1
- update to 4.0.3 (no change)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 4.0.2-1
- update to 4.0.2

* Tue Jun 16 2020 Remi Collet <remi@remirepo.net> - 4.0.1-1
- update to 4.0.1
- sources from git snapshot
- drop patch merged upstream

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 4.0.0-1
- update to 4.0.0
- raise dependency on PHP 7.3
- raise dependency on sebastian/object-reflector 2
- raise dependency on sebastian/recursion-context 4
- rename to php-sebastian-object-enumerator4
- move to /usr/share/php/SebastianBergmann/ObjectEnumerator4
- fix test suite with patch from
  https://github.com/sebastianbergmann/object-enumerator/pull/8

* Thu Dec  6 2018 Remi Collet <remi@remirepo.net> - 3.0.3-3
- cleanup for EL-8

* Tue Feb  6 2018 Remi Collet <remi@remirepo.net> - 3.0.3-2
- use range dependencies on F27+

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 3.0.3-1
- Update to 3.0.3 - no change
- raise dependency on sebastian/object-reflector 1.1.1

* Sun Mar 12 2017 Remi Collet <remi@remirepo.net> - 3.0.2-1
- Update to 3.0.2
- add dependency on sebastian/object-reflector

* Sun Mar 12 2017 Remi Collet <remi@remirepo.net> - 3.0.1-1
- Update to 3.0.1

* Fri Mar  3 2017 Remi Collet <remi@fedoraproject.org> - 3.0.0-1
- update to 3.0.0
- rename to php-sebastian-object-enumerator3
- raise dependency on PHP 7
- raise dependency on recursion-context 3

* Sat Feb 18 2017 Remi Collet <remi@fedoraproject.org> - 2.0.1-1
- update to 2.0.1

* Tue Nov 22 2016 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 2.0.0 (no change)
- raise dependency on sebastian/recursion-context 2.0

* Wed Nov 16 2016 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1
- raise dependency on sebastian/recursion-context 1.0.4

* Mon Oct 31 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- switch to fedora/autoloader

* Wed Mar 23 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package
