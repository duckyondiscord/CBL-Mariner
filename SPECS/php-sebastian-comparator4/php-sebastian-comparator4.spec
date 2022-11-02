# remirepo/fedora spec file for php-sebastian-comparator4
#
# Copyright (c) 2014-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# Namespace
%global php_home     %{_datadir}/php

Name:           php-sebastian-comparator4
Version:        4.0.8
Release:        1%{?dist}
Summary:        Compare PHP values for equality, version 4

License:        BSD
URL:            https://github.com/sebastianbergmann/comparator
Source0:        https://github.com/sebastianbergmann/comparator/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz


BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  (php-composer(sebastian/diff)     >= 4.0   with php-composer(sebastian/diff)     < 5)
BuildRequires:  (php-composer(sebastian/exporter) >= 4.0   with php-composer(sebastian/exporter) < 5)
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.3"
BuildRequires:  phpunit9 >= 9.3
%endif

# from composer.json
#        "php": ">=7.3",
#        "sebastian/diff": "^4.0",
#        "sebastian/exporter": "^4.0"
Requires:       php(language) >= 7.3
Requires:       (php-composer(sebastian/diff)     >= 4.0   with php-composer(sebastian/diff)     <  5)
Requires:       (php-composer(sebastian/exporter) >= 4.0   with php-composer(sebastian/exporter) <  5)
# from phpcompatinfo report for version 4.0.0
Requires:       php-date
Requires:       php-dom
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(sebastian/comparator) = %{version}


%description
This component provides the functionality to compare PHP values for equality.

Autoloader: %{php_home}/SebastianBergmann/Comparator4/autoload.php


%prep
%setup -q 


%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src

# Rely on include_path as in PHPUnit dependencies
cat <<EOF | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/SebastianBergmann/Diff4/autoload.php',
    '%{php_home}/SebastianBergmann/Exporter4/autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{php_home}/SebastianBergmann
cp -pr src %{buildroot}%{php_home}/SebastianBergmann/Comparator4


%check
%if %{with tests}
mkdir vendor
%{_bindir}/phpab --template fedora --output vendor/autoload.php tests/_fixture

: Run upstream test suite
ret=0
for cmd in php php74 php80 php81 php82; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/SebastianBergmann/Comparator4/autoload.php \
      %{_bindir}/phpunit9 --no-coverage --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%doc README.md composer.json
%license LICENSE
%{php_home}/SebastianBergmann/Comparator4


%changelog
* Wed Sep 14 2022 Remi Collet <remi@remirepo.net> - 4.0.8-1
- update to 4.0.8

* Wed Sep 14 2022 Remi Collet <remi@remirepo.net> - 4.0.7-1
- update to 4.0.7

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Remi Collet <remi@remirepo.net> - 4.0.6-1
- update to 4.0.6

* Wed Sep 30 2020 Remi Collet <remi@remirepo.net> - 4.0.5-1
- update to 4.0.5

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 4.0.4-1
- update to 4.0.4 (no change)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 4.0.3-1
- update to 4.0.3

* Tue Jun 16 2020 Remi Collet <remi@remirepo.net> - 4.0.2-1
- update to 4.0.2
- sources from git snapshot

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 4.0.0-1
- update to 4.0.0
- raise dependency on PHP 7.3
- raise dependency on sebastian/diff 4
- raise dependency on sebastian/exporter 4
- rename to php-sebastian-comparator4
- move to /usr/share/php/SebastianBergmann/Comparator4

* Thu Jul 12 2018 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2

* Tue Jun 19 2018 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1

* Wed Apr 18 2018 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- rename to php-sebastian-comparator3
- raise dependency on PHP 7.1
- raise dependency on sebastian/diff 3.0
- use phpunit7

* Fri Feb  2 2018 Remi Collet <remi@remirepo.net> - 2.1.3-1
- Update to 2.1.3 (no change)
- allow sebastian/diff v3
- use range dependencies on F27+

* Fri Jan 12 2018 Remi Collet <remi@remirepo.net> - 2.1.2-1
- Update to 2.1.2

* Sat Dec 23 2017 Remi Collet <remi@remirepo.net> - 2.1.1-1
- Update to 2.1.1

* Fri Nov  3 2017 Remi Collet <remi@remirepo.net> - 2.1.0-1
- Update to 2.1.0
- raise dependency on sebastian/exporter 3.1

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 2.0.2-1
- Update to 2.0.2
- raise dependency on sebastian/diff 2.0
- raise various dependencies on latest minor version

* Wed Jul 12 2017 Remi Collet <remi@remirepo.net> - 2.0.1-1
- Update to 2.0.1

* Fri Mar  3 2017 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 3.0.0
- rename to php-sebastian-comparator2
- raise dependency on PHP 7
- raise dependency on sebastian/exporter 3

* Sun Jan 29 2017 Remi Collet <remi@fedoraproject.org> - 1.2.4-1
- update to 1.2.4

* Sun Jan 29 2017 Remi Collet <remi@fedoraproject.org> - 1.2.3-1
- update to 1.2.3

* Tue Nov 22 2016 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- update to 1.2.2 (no change)
- allow sebastian/exporter 2.0

* Thu Nov 17 2016 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1
- switch to fedora/autoloader

* Sun Jul 26 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0

* Mon Jun 29 2015 Remi Collet <remi@fedoraproject.org> - 1.1.1-3
- manage dependencies in autoloader

* Fri Jan 30 2015 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1
- raise dependency on sebastian/diff >= 1.2
- raise dependency on sebastian/exporter >= 1.2

* Thu Dec  4 2014 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0

* Sun Oct  5 2014 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1
- enable test suite

* Fri Jul 18 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- add composer dependencies

* Sat May  3 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package
