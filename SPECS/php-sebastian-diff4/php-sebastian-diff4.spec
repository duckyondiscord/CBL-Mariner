# remirepo/fedora spec file for php-sebastian-diff4
#
# Copyright (c) 2013-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Namespace
%global php_home     %{_datadir}/php

Name:           php-sebastian-diff4
Version:        4.0.4
Release:        5%{?dist}
Summary:        Diff implementation, version 4

License:        BSD
URL:            https://github.com/sebastianbergmann/diff
Source0:        https://github.com/sebastianbergmann/diff/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with_check}
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-pcre
BuildRequires:  php-spl
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.3",
#        "symfony/process": "^4.2 || ^5"
BuildRequires:  phpunit9 >= 9.3
BuildRequires:  php-symfony4-process
%endif

# from composer.json
#        "php": ">=7.3"
Requires:       php(language) >= 7.3
# from phpcompatinfo report for version 4.0.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sebastian/diff) = %{version}


%description
Diff implementation.

Autoloader: %{php_home}/SebastianBergmann/Diff4/autoload.php


%prep
%setup -q


%build
# Generate the Autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src


%install
mkdir -p   %{buildroot}%{php_home}/SebastianBergmann
cp -pr src %{buildroot}%{php_home}/SebastianBergmann/Diff4


%check
%if %{with_check}
mkdir vendor
%{_bindir}/phpab --output vendor/autoload.php tests
cat << 'EOF' | tee -a vendor/autoload.php
\Fedora\Autoloader\Dependencies::required([
    [
        '%{php_home}/Symfony5/Component/Process/autoload.php',
        '%{php_home}/Symfony4/Component/Process/autoload.php',
    ]
]);
EOF


: Run upstream test suite
ret=0
for cmd in php php73 php74 php80 php81; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/SebastianBergmann/Diff4/autoload.php \
      %{_bindir}/phpunit9  --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc *.md
%dir %{php_home}/SebastianBergmann
     %{php_home}/SebastianBergmann/Diff4


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Remi Collet <remi@remirepo.net> - 4.0.4-1
- update to 4.0.4

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 4.0.3-1
- update to 4.0.3 (no change)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Remi Collet <remi@remirepo.net> - 4.0.2-1
- update to 4.0.2

* Fri May  8 2020 Remi Collet <remi@remirepo.net> - 4.0.1-1
- update to 4.0.1
- sources from git snapshot
- switch to phpunit9

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 4.0.0-1
- update to 4.0.0
- raise dependency on PHP 7.3
- rename to php-sebastian-diff4
- move to /usr/share/php/SebastianBergmann/Diff4

* Mon Feb  4 2019 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2

* Mon Jun 11 2018 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1 (no change)
- ignore integration tests with old git command

* Wed Feb  7 2018 Remi Collet <remi@remirepo.net> - 3.0.0-1
- normal build

* Fri Feb  2 2018 Remi Collet <remi@remirepo.net> - 3.0.0-0
- update to 3.0.0
- renamed to php-sebastian-diff3
- move to /usr/share/php/SebastianBergmann/Diff3
- raise dependency on PHP 7.1
- use phpunit7
- boostrap build

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1
- renamed to php-sebastian-diff2
- raise dependency on PHP 7.0

* Mon May 22 2017 Remi Collet <remi@remirepo.net> - 1.4.3-1
- Update to 1.4.3

* Mon May 22 2017 Remi Collet <remi@remirepo.net> - 1.4.2-1
- Update to 1.4.2
- switch to fedora/autoloader
- use PHPUnit 6 when available

* Sun Dec  6 2015 Remi Collet <remi@fedoraproject.org> - 1.4.0-1
- update to 1.4.1 (no change)
- run test suite with both php 5 and 7 when available

* Fri Apr  3 2015 Remi Collet <remi@fedoraproject.org> - 1.3.0-1
- update to 1.3.0

* Fri Oct  3 2014 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0
- run test suite during build
- generate autoload.php for compatibility
- fix license handling

* Wed Jun 25 2014 Remi Collet <remi@fedoraproject.org> - 1.1.0-6
- composer dependencies

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.1.0-4
- cleanup pear registry

* Wed Apr 23 2014 Remi Collet <remi@fedoraproject.org> - 1.1.0-3
- get sources from github
- run test suite when build --with tests

* Sun Oct 20 2013 Remi Collet <remi@fedoraproject.org> - 1.1.0-2
- rename to lowercase

* Thu Sep 12 2013 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- initial package