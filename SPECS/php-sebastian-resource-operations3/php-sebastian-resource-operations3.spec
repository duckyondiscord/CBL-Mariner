# remirepo/fedora spec file for php-sebastian-resource-operations3
#
# Copyright (c) 2015-2020 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global php_home     %{_datadir}/php

Name:           php-sebastian-resource-operations3
Version:        3.0.3
Release:        2
Summary:        Provides a list of PHP built-in functions that operate on resources, version 3

License:        BSD
URL:            https://github.com/sebastianbergmann/resource-operations
Source0:        https://github.com/sebastianbergmann/resource-operations/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-fedora-autoloader-devel
%if %{with_check}
# from composer.json
#        "phpunit/phpunit": "^9.0"
BuildRequires:  phpunit9
%endif

# from composer.json
#        "php": ">=7.3"
Requires:       php(language) >= 7.3
# Autoloader
Requires:       php-composer(fedora/autoloader)
# from phpcompatinfo report for version 3.0.0: nothing

Provides:       php-composer(sebastian/resource-operations) = %{version}


%description
%{summary}.

This package provides version 3.

Autoloader: %{php_home}/SebastianBergmann/ResourceOperations3/autoload.php


%prep
%setup -q


%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src


%install
mkdir -p   %{buildroot}%{php_home}/SebastianBergmann
cp -pr src %{buildroot}%{php_home}/SebastianBergmann/ResourceOperations3


%check
%if %{with_check}
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php73 php74 php80 php81; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/SebastianBergmann/ResourceOperations3/autoload.php \
      %{_bindir}/phpunit9  --verbose tests || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md composer.json
%dir %{php_home}/SebastianBergmann
     %{php_home}/SebastianBergmann/ResourceOperations3


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-1.2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 3.0.3-1
- update to 3.0.3 (no change)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2 (no change)

* Tue Jun 16 2020 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1 (no change)
- sources from git snapshot

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- raise dependency on PHP 7.3
- rename to php-sebastian-resource-operations3
- move to /usr/share/php/SebastianBergmann/ResourceOperations3

* Thu Oct  4 2018 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1
- drop patch merged upstream

* Fri Sep 28 2018 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- raise dependency on PHP 7.1
- rename to php-sebastian-resource-operations2
- move to /usr/share/php/SebastianBergmann/ResourceOperations2

* Mon Oct 31 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- switch to fedora/autoloader

* Fri Oct  2 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0 (no change)

* Tue Sep 29 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.20150728gitce990bb
- initial package
