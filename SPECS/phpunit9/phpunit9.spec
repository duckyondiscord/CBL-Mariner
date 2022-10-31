# For compatibility with SCL
%undefine __brp_mangle_shebangs

# Namespace
%global ns_vendor    PHPUnit9
%global php_home     %{_datadir}/php

Name:           phpunit9
Version:        9.5.26
Release:        1%{?dist}
Summary:        The PHP Unit Testing framework version 9

License:        BSD
URL:            https://github.com/sebastianbergmann/phpunit
Source0:        https://github.com/sebastianbergmann/phpunit/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source1:        makesrc.sh

# Fix command for autoload
Patch0:         phpunit9-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  (php-composer(doctrine/instantiator) >= 1.3.1         with php-composer(doctrine/instantiator) <  2)
BuildRequires:  (php-composer(myclabs/deep-copy) >= 1.10.1            with php-composer(myclabs/deep-copy) <  2)
BuildRequires:  (php-composer(phar-io/manifest) >= 2.0.3              with php-composer(phar-io/manifest) < 3)
BuildRequires:  (php-composer(phar-io/version) >= 3.0.2               with php-composer(phar-io/version) <  4)
BuildRequires:  (php-composer(phpspec/prophecy) >= 1.12.1             with php-composer(phpspec/prophecy) <  2)
BuildRequires:  (php-composer(phpunit/php-code-coverage) >= 9.2.13    with php-composer(phpunit/php-code-coverage) <  10)
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 3.0.4     with php-composer(phpunit/php-file-iterator) <  4)
BuildRequires:  (php-composer(phpunit/php-invoker) >= 3.1             with php-composer(phpunit/php-invoker) <  4)
BuildRequires:  (php-composer(phpunit/php-text-template) >= 2.0.2     with php-composer(phpunit/php-text-template) <  3)
BuildRequires:  (php-composer(phpunit/php-timer) >= 5.0.1             with php-composer(phpunit/php-timer) < 6)
BuildRequires:  (php-composer(sebastian/cli-parser) >= 1.0            with php-composer(sebastian/cli-parser) < 2)
BuildRequires:  (php-composer(sebastian/code-unit) >= 1.0.5           with php-composer(sebastian/code-unit) < 2)
BuildRequires:  (php-composer(sebastian/comparator) >= 4.0.8          with php-composer(sebastian/comparator) <  5)
BuildRequires:  (php-composer(sebastian/diff) >= 4.0.2                with php-composer(sebastian/diff) <  5)
BuildRequires:  (php-composer(sebastian/environment) >= 5.1.2         with php-composer(sebastian/environment) <  6)
BuildRequires:  (php-composer(sebastian/exporter) >= 4.0.5            with php-composer(sebastian/exporter) <  5)
BuildRequires:  (php-composer(sebastian/global-state) >= 5.0          with php-composer(sebastian/global-state) <  6)
BuildRequires:  (php-composer(sebastian/object-enumerator) >= 4.0.2   with php-composer(sebastian/object-enumerator) <  5)
BuildRequires:  (php-composer(sebastian/resource-operations) >= 3.0.2 with php-composer(sebastian/resource-operations) < 4)
BuildRequires:  (php-composer(sebastian/type) >= 3.2                  with php-composer(sebastian/type) < 4)
BuildRequires:  (php-composer(sebastian/version) >= 3.0.1             with php-composer(sebastian/version) <  4)
BuildRequires:  php-dom
BuildRequires:  php-json
BuildRequires:  php-mbstring
BuildRequires:  php-xml
BuildRequires:  php-libxml
BuildRequires:  php-xmlwriter
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0

# From composer.json, "require": {
#        "php": ">=7.3",
#        "ext-dom": "*",
#        "ext-json": "*",
#        "ext-libxml": "*",
#        "ext-mbstring": "*",
#        "ext-xml": "*",
#        "ext-xmlwriter": "*",
#        "doctrine/instantiator": "^1.3.1",
#        "myclabs/deep-copy": "^1.10.1",
#        "phar-io/manifest": "^2.0.3",
#        "phar-io/version": "^3.0.2",
#        "phpunit/php-code-coverage": "^9.2.13",
#        "phpunit/php-file-iterator": "^3.0.5",
#        "phpunit/php-invoker": "^3.1.1",
#        "phpunit/php-text-template": "^2.0.3",
#        "phpunit/php-timer": "^5.0.2",
#        "sebastian/cli-parser": "^1.0.1",
#        "sebastian/code-unit": "^1.0.6",
#        "sebastian/comparator": "^4.0.8",
#        "sebastian/diff": "^4.0.3",
#        "sebastian/environment": "^5.1.3",
#        "sebastian/exporter": "^4.0.5",
#        "sebastian/global-state": "^5.0.1",
#        "sebastian/object-enumerator": "^4.0.3",
#        "sebastian/resource-operations": "^3.0.3",
#        "sebastian/type": "^3.2",
#        "sebastian/version": "^3.0.2"
Requires:       php(language) >= 7.3
Requires:       php-cli
Requires:       php-dom
Requires:       php-json
Requires:       php-libxml
Requires:       php-mbstring
Requires:       php-xml
Requires:       php-xmlwriter
Requires:       (php-composer(doctrine/instantiator) >= 1.3.1         with php-composer(doctrine/instantiator) <  2)
Requires:       (php-composer(myclabs/deep-copy) >= 1.10.1            with php-composer(myclabs/deep-copy) <  2)
Requires:       (php-composer(phar-io/manifest) >= 2.0.3              with php-composer(phar-io/manifest) < 3)
Requires:       (php-composer(phar-io/version) >= 3.0.2               with php-composer(phar-io/version) < 4)
Requires:       (php-composer(phpspec/prophecy) >= 1.12.1             with php-composer(phpspec/prophecy) <  2)
Requires:       (php-composer(phpunit/php-code-coverage) >= 9.2.13    with php-composer(phpunit/php-code-coverage) <  10)
Requires:       (php-composer(phpunit/php-file-iterator) >= 3.0.4     with php-composer(phpunit/php-file-iterator) <  4)
Requires:       (php-composer(phpunit/php-invoker) >= 3.1             with php-composer(phpunit/php-invoker) <  4)
Requires:       (php-composer(phpunit/php-text-template) >= 2.0.2     with php-composer(phpunit/php-text-template) <  3)
Requires:       (php-composer(phpunit/php-timer) >= 5.0.1             with php-composer(phpunit/php-timer) < 6)
Requires:       (php-composer(sebastian/cli-parser) >= 1.0            with php-composer(sebastian/cli-parser) < 2)
Requires:       (php-composer(sebastian/code-unit) >= 1.0.5           with php-composer(sebastian/code-unit) < 2)
Requires:       (php-composer(sebastian/comparator) >= 4.0.8          with php-composer(sebastian/comparator) <  5)
Requires:       (php-composer(sebastian/diff) >= 4.0.2                with php-composer(sebastian/diff) <  5)
Requires:       (php-composer(sebastian/environment) >= 5.1.2         with php-composer(sebastian/environment) <  6)
Requires:       (php-composer(sebastian/exporter) >= 4.0.5            with php-composer(sebastian/exporter) <  5)
Requires:       (php-composer(sebastian/global-state) >= 5.0          with php-composer(sebastian/global-state) <  6)
Requires:       (php-composer(sebastian/object-enumerator) >= 4.0.2   with php-composer(sebastian/object-enumerator) <  5)
Requires:       (php-composer(sebastian/resource-operations) >= 3.0.2 with php-composer(sebastian/resource-operations) <  4)
Requires:       (php-composer(sebastian/type) >= 3.2                  with php-composer(sebastian/type) < 4)
Requires:       (php-composer(sebastian/version) >= 3.0.1             with php-composer(sebastian/version) <  4)
# From composer.json, "suggest": {
#        "ext-soap": "*",
#        "ext-xdebug": "*"
Suggests:       php-soap
Suggests:       php-xdebug
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 8.0.0
Requires:       php-reflection
Requires:       php-openssl
Requires:       php-pcntl
Requires:       php-pcre
Requires:       php-phar
Requires:       php-spl


%description
PHPUnit is a programmer-oriented testing framework for PHP.
It is an instance of the xUnit architecture for unit testing frameworks.

This package provides the version 9 of PHPUnit,
available using the %{name} command.

Documentation: https://phpunit.readthedocs.io/


%prep
%setup -q
%patch0 -p0 -b .rpm

find . -name \*.rpm -delete -print


%build
%{_bindir}/phpab \
  --template fedora2 \
  --output   src/autoload.php \
  src

cat << 'EOF' | tee -a src/autoload.php
// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/SebastianBergmann/CodeCoverage9/autoload.php',
    '%{php_home}/SebastianBergmann/FileIterator3/autoload.php',
    '%{php_home}/SebastianBergmann/Template2/autoload.php',
    '%{php_home}/SebastianBergmann/Timer5/autoload.php',
    '%{php_home}/Prophecy/autoload.php',
    '%{php_home}/SebastianBergmann/CliParser/autoload.php',
    '%{php_home}/SebastianBergmann/CodeUnit/autoload.php',
    '%{php_home}/SebastianBergmann/Invoker3/autoload.php',
    '%{php_home}/SebastianBergmann/Diff4/autoload.php',
    '%{php_home}/SebastianBergmann/Comparator4/autoload.php',
    '%{php_home}/SebastianBergmann/Environment5/autoload.php',
    '%{php_home}/SebastianBergmann/Exporter4/autoload.php',
    '%{php_home}/SebastianBergmann/GlobalState5/autoload.php',
    '%{php_home}/SebastianBergmann/ObjectEnumerator4/autoload.php',
    '%{php_home}/SebastianBergmann/ResourceOperations3/autoload.php',
    '%{php_home}/SebastianBergmann/Type3/autoload.php',
    '%{php_home}/SebastianBergmann/Version3/autoload.php',
    '%{php_home}/Doctrine/Instantiator/autoload.php',
    '%{php_home}/DeepCopy/autoload.php',
    '%{php_home}/PharIo/Manifest2/autoload.php',
    '%{php_home}/PharIo/Version3/autoload.php',
    __DIR__ . '/Framework/Assert/Functions.php',
]);
// Extensions
\Fedora\Autoloader\Dependencies::optional(
    glob("%{php_home}/%{ns_vendor}/Extensions/*/autoload.php")
);
EOF
cat src/autoload.php

%{_bindir}/phpab \
  --output   tests/autoload.php \
  --exclude  'tests/end-to-end/regression/4376/tests/Test.php' \
  --exclude  'tests/end-to-end/regression/2448/Test.php' \
  --exclude  'tests/end-to-end/migration/_files/possibility-to-migrate-from-85-is-detected/src/Greeter.php' \
  --exclude  'tests/end-to-end/migration/_files/possibility-to-migrate-from-85-is-detected/tests/GreeterTest.php' \
  tests


%install
mkdir -p       %{buildroot}%{php_home}
cp -pr src     %{buildroot}%{php_home}/%{ns_vendor}
cp -pr schema  %{buildroot}%{php_home}/%{ns_vendor}/schema
mkdir          %{buildroot}%{php_home}/%{ns_vendor}/Extensions

install -D -p -m 755 phpunit %{buildroot}%{_bindir}/%{name}
install -p -m 644 phpunit.xsd %{buildroot}%{php_home}/%{ns_vendor}/phpunit.xsd


%check
OPT="--testsuite=unit --no-coverage"
sed -e 's:@PATH@:%{buildroot}%{php_home}/%{ns_vendor}:' -i tests/bootstrap.php
sed -e 's:%{php_home}/%{ns_vendor}:%{buildroot}%{php_home}/%{ns_vendor}:' -i phpunit

ret=0
for cmd in php php74 php80 php81 php82; do
  if which $cmd; then
     $cmd ./phpunit $OPT --verbose || ret=1
  fi
done
exit $ret


%files
%license LICENSE
%doc README.md ChangeLog-9.5.md
%doc composer.json
%{_bindir}/%{name}
%{php_home}/%{ns_vendor}


%changelog
* Fri Oct 28 2022 Osama Esmail <osamaesmail@microsoft.com> - 9.5.26-2
- Initial CBL-Mariner import from Fedora 36 (license: MIT).
- License verified.

* Fri Oct 28 2022 Remi Collet <remi@remirepo.net> - 9.5.26-1
- update to 9.5.26

* Sun Sep 25 2022 Remi Collet <remi@remirepo.net> - 9.5.25-1
- update to 9.5.25
- raise dependency on sebastian/comparator 4.0.8
- raise dependency on sebastian/exporter 4.0.5
- raise dependency on sebastian/type 3.2

* Thu Sep  1 2022 Remi Collet <remi@remirepo.net> - 9.5.24-1
- update to 9.5.24
- raise dependency on sebastian/type 3.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Remi Collet <remi@remirepo.net> - 9.5.21-1
- update to 9.5.21
- raise dependency on sebastian/type 3.0

* Tue Mar  8 2022 Remi Collet <remi@remirepo.net> - 9.5.18-1
- update to 9.5.18

* Sun Mar  6 2022 Remi Collet <remi@remirepo.net> - 9.5.17-1
- update to 9.5.17 #StandWithUkraine

* Thu Feb 24 2022 Remi Collet <remi@remirepo.net> - 9.5.16-1
- update to 9.5.16
- raise dependency on phpunit/php-code-coverage 9.2.13

* Wed Feb 23 2022 Remi Collet <remi@remirepo.net> - 9.5.15-1
- update to 9.5.15
- raise dependency on phpunit/php-code-coverage 9.2.12

* Fri Feb 18 2022 Remi Collet <remi@remirepo.net> - 9.5.14-1
- update to 9.5.14

* Mon Jan 24 2022 Remi Collet <remi@remirepo.net> - 9.5.13-1
- update to 9.5.13

* Fri Jan 21 2022 Remi Collet <remi@remirepo.net> - 9.5.12-1
- update to 9.5.12

* Thu Dec 30 2021 Remi Collet <remi@remirepo.net> - 9.5.11-1
- update to 9.5.11

* Mon Sep 27 2021 Remi Collet <remi@remirepo.net> - 9.5.10-1
- update to 9.5.10
- raise dependency on phpunit/php-code-coverage 9.2.7

* Wed Sep  1 2021 Remi Collet <remi@remirepo.net> - 9.5.9-1
- update to 9.5.9

* Mon Aug  2 2021 Remi Collet <remi@remirepo.net> - 9.5.8-1
- update to 9.5.8
- raise dependency on phar-io/manifest 2.0.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 19 2021 Remi Collet <remi@remirepo.net> - 9.5.7-1
- update to 9.5.7

* Wed Jun 23 2021 Remi Collet <remi@remirepo.net> - 9.5.6-1
- update to 9.5.6

* Mon Jun  7 2021 Remi Collet <remi@remirepo.net> - 9.5.5-1
- update to 9.5.5
- raise dependency on sebastian/type 2.3.2

* Tue Mar 23 2021 Remi Collet <remi@remirepo.net> - 9.5.4-1
- update to 9.5.4

* Wed Mar 17 2021 Remi Collet <remi@remirepo.net> - 9.5.3-1
- update to 9.5.3

* Wed Feb  3 2021 Remi Collet <remi@remirepo.net> - 9.5.2-1
- update to 9.5.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec  4 2020 Remi Collet <remi@remirepo.net> - 9.5.0-1
- update to 9.5.0
- raise dependency on phpunit/php-code-coverage 9.2.3

* Tue Dec  1 2020 Remi Collet <remi@remirepo.net> - 9.4.4-1
- update to 9.4.4

* Tue Nov 10 2020 Remi Collet <remi@remirepo.net> - 9.4.3-1
- update to 9.4.3

* Mon Oct 19 2020 Remi Collet <remi@remirepo.net> - 9.4.2-1
- update to 9.4.2

* Mon Oct 12 2020 Remi Collet <remi@remirepo.net> - 9.4.1-1
- update to 9.4.1

* Fri Oct  2 2020 Remi Collet <remi@remirepo.net> - 9.4.0-1
- update to 9.4.0
- raise dependency on phpunit/php-code-coverage 9.2

* Thu Sep 24 2020 Remi Collet <remi@remirepo.net> - 9.3.11-1
- update to 9.3.11 (no change)
- raise dependency on phpunit/php-code-coverage 9.1.11

* Sun Sep 13 2020 Remi Collet <remi@remirepo.net> - 9.3.10-1
- update to 9.3.10

* Thu Aug 27 2020 Remi Collet <remi@remirepo.net> - 9.3.8-1
- update to 9.3.8
- add dependency on sebastian/cli-parser
- raise dependency on phpunit/php-code-coverage 9.1.5
- raise dependency on myclabs/deep-copy 1.10.1
- raise dependency on phar-io/manifest 2.0.1
- raise dependency on phar-io/version 3.0.2
- raise dependency on phpspec/prophecy 1.11.1
- raise dependency on phpunit/php-file-iterator 3.0.4
- raise dependency on phpunit/php-invoker 3.1
- raise dependency on sebastian/diff 4.0.2
- raise dependency on sebastian/global-state 5.0
- raise dependency on sebastian/type 2.2.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.6-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Remi Collet <remi@remirepo.net> - 9.2.6-1
- update to 9.2.6
- raise dependency on latest minor version available
  for all libraries

* Mon Jun 22 2020 Remi Collet <remi@remirepo.net> - 9.2.5-1
- update to 9.2.5
- raise dependency on phpunit/php-timer 5.0
- raise dependency on sebastian/type 2.1

* Sat May 23 2020 Remi Collet <remi@remirepo.net> - 9.1.5-1
- update to 9.1.5
- sources from git snapshot

* Thu Apr 30 2020 Remi Collet <remi@remirepo.net> - 9.1.4-1
- update to 9.1.4
- raise dependency on sebastian/code-unit 1.0.2

* Thu Apr 23 2020 Remi Collet <remi@remirepo.net> - 9.1.3-1
- update to 9.1.3
- raise dependency on phpunit/php-timer 3.1.4
- add dependency on sebastian/code-unit

* Tue Mar 31 2020 Remi Collet <remi@remirepo.net> - 9.0.2-1
- update to 9.0.2
- own /usr/share/php/PHPUnit9/Extensions
- raise dependency on phpunit/php-code-coverage 8.0.1
- raise dependency on sebastian/environment 5.0.1

* Fri Feb 14 2020 Remi Collet <remi@remirepo.net> - 9.0.1-1
- update to 9.0.1

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 9.0.0-1
- update to 9.0.0
- raise dependency on PHP 7.3
- raise dependency on phpunit/php-code-coverage 8
- raise dependency on phpunit/php-file-iterator 3
- raise dependency on phpunit/php-text-template 2
- raise dependency on phpunit/php-timer 3
- raise dependency on sebastian/comparator 4
- raise dependency on sebastian/diff 4
- raise dependency on sebastian/environment 5
- raise dependency on sebastian/exporter 4
- raise dependency on sebastian/global-state 4
- raise dependency on sebastian/object-enumerator 4
- raise dependency on sebastian/resource-operations 3
- raise dependency on sebastian/type 2
- raise dependency on sebastian/version 3
- add dependency on phpunit/php-invoker 3
- rename to phpunit9
- move to /usr/share/php/PHPUnit9

* Wed Jan  8 2020 Remi Collet <remi@remirepo.net> - 8.5.2-1
- update to 8.5.2

* Thu Jan  2 2020 Remi Collet <remi@remirepo.net> - 8.5.1-1
- update to 8.5.1

* Fri Dec  6 2019 Remi Collet <remi@remirepo.net> - 8.5.0-1
- update to 8.5.0

* Wed Nov  6 2019 Remi Collet <remi@remirepo.net> - 8.4.3-1
- update to 8.4.3

* Mon Oct 28 2019 Remi Collet <remi@remirepo.net> - 8.4.2-1
- update to 8.4.2

* Tue Oct  8 2019 Remi Collet <remi@remirepo.net> - 8.4.1-1
- update to 8.4.1

* Fri Oct  4 2019 Remi Collet <remi@remirepo.net> - 8.4.0-1
- update to 8.4.0

* Sun Sep 15 2019 Remi Collet <remi@remirepo.net> - 8.3.5-1
- update to 8.3.5
- raise dependency on sebastian/exporter 3.1.1

* Mon Aug 12 2019 Remi Collet <remi@remirepo.net> - 8.3.4-1
- update to 8.3.4

* Sun Aug  4 2019 Remi Collet <remi@remirepo.net> - 8.3.3-1
- update to 8.3.3

* Sat Aug  3 2019 Remi Collet <remi@remirepo.net> - 8.3.2-1
- update to 8.3.2

* Fri Aug  2 2019 Remi Collet <remi@remirepo.net> - 8.3.0-1
- update to 8.3.0
- raise dependency on phpunit/php-code-coverage 7.0.7

* Mon Jul 15 2019 Remi Collet <remi@remirepo.net> - 8.2.5-1
- update to 8.2.5

* Wed Jul  3 2019 Remi Collet <remi@remirepo.net> - 8.2.4-1
- update to 8.2.4
- raise dependency on sebastian/type 1.1.3

* Wed Jun 19 2019 Remi Collet <remi@remirepo.net> - 8.2.3-1
- update to 8.2.3

* Sun Jun 16 2019 Remi Collet <remi@remirepo.net> - 8.2.2-1
- update to 8.2.2 (no change)
- raise dependency on phpspec/prophecy 1.8.1

* Sat Jun  8 2019 Remi Collet <remi@remirepo.net> - 8.2.1-1
- update to 8.2.1
- raise dependency on sebastian/type 1.1.0

* Fri Jun  7 2019 Remi Collet <remi@remirepo.net> - 8.2.0-1
- update to 8.2.0
- add dependency on sebastian/type
- raise dependency on doctrine/instantiator 1.2.0
- raise dependency on myclabs/deep-copy 1.9.1
- raise dependency on phar-io/manifest 1.0.3
- raise dependency on phar-io/version 2.0.1
- raise dependency on phpspec/prophecy 1.8.0
- raise dependency on phpunit/php-code-coverage 7.0.5
- raise dependency on phpunit/php-file-iterator 2.0.2
- raise dependency on phpunit/php-timer 2.1.2
- raise dependency on sebastian/comparator 3.0.2
- raise dependency on sebastian/diff 3.0.2
- raise dependency on sebastian/environment 4.2.2
- raise dependency on sebastian/resource-operations 2.0.1

* Tue May 28 2019 Remi Collet <remi@remirepo.net> - 8.1.6-1
- update to 8.1.6

* Tue May 14 2019 Remi Collet <remi@remirepo.net> - 8.1.5-1
- update to 8.1.5

* Fri May 10 2019 Remi Collet <remi@remirepo.net> - 8.1.4-1
- update to 8.1.4

* Tue Apr 23 2019 Remi Collet <remi@remirepo.net> - 8.1.3-1
- update to 8.1.3

* Tue Apr  9 2019 Remi Collet <remi@remirepo.net> - 8.1.2-1
- update to 8.1.2

* Mon Apr  8 2019 Remi Collet <remi@remirepo.net> - 8.1.1-1
- update to 8.1.1

* Fri Apr  5 2019 Remi Collet <remi@remirepo.net> - 8.1.0-1
- update to 8.1.0

* Wed Mar 27 2019 Remi Collet <remi@remirepo.net> - 8.0.6-1
- update to 8.0.6

* Sat Mar 16 2019 Remi Collet <remi@remirepo.net> - 8.0.5-1
- update to 8.0.5
- raise dependency on phpunit/php-timer 2.1

* Mon Feb 18 2019 Remi Collet <remi@remirepo.net> - 8.0.4-1
- update to 8.0.4

* Sat Feb 16 2019 Remi Collet <remi@remirepo.net> - 8.0.3-1
- update to 8.0.3

* Fri Feb  8 2019 Remi Collet <remi@remirepo.net> - 8.0.2-1
- update to 8.0.2

* Mon Feb  4 2019 Remi Collet <remi@remirepo.net> - 8.0.1-1
- update to 8.0.1

* Fri Feb  1 2019 Remi Collet <remi@remirepo.net> - 8.0.0-1
- rename to phpunit8
- update to 8.0.0
- add dependency on xmlwriter extension
- add weak dependency on soap, xdebug extension
- raise dependency on PHP 7.2
- raise dependency on phpunit/php-code-coverage 7.0
- raise dependency on sebastian/environment 4.1
- raise dependency on sebastian/global-state 3.0

* Fri Feb  1 2019 Remi Collet <remi@remirepo.net> - 7.5.3-1
- update to 7.5.3

* Tue Jan 15 2019 Remi Collet <remi@remirepo.net> - 7.5.2-1
- update to 7.5.2

* Wed Dec 12 2018 Remi Collet <remi@remirepo.net> - 7.5.1-1
- update to 7.5.1

* Fri Dec  7 2018 Remi Collet <remi@remirepo.net> - 7.5.0-1
- update to 7.5.0

* Mon Dec  3 2018 Remi Collet <remi@remirepo.net> - 7.4.5-1
- update to 7.4.5
- raise dependency on sebastian/environment 4.0

* Thu Nov 15 2018 Remi Collet <remi@remirepo.net> - 7.4.4-1
- update to 7.4.4

* Tue Oct 23 2018 Remi Collet <remi@remirepo.net> - 7.4.3-1
- update to 7.4.3
- drop patch merged upstream

* Thu Oct 18 2018 Remi Collet <remi@remirepo.net> - 7.4.1-2
- add patch for https://github.com/sebastianbergmann/phpunit/issues/3354
  from https://github.com/sebastianbergmann/phpunit/pull/3355

* Thu Oct 18 2018 Remi Collet <remi@remirepo.net> - 7.4.1-1
- update to 7.4.1
- allow sebastian/environment 4

* Fri Oct  5 2018 Remi Collet <remi@remirepo.net> - 7.4.0-1
- update to 7.4.0
- raise dependency on sebastian/resource-operations 2.0

* Sun Sep  9 2018 Remi Collet <remi@remirepo.net> - 7.3.5-1
- update to 7.3.5

* Wed Sep  5 2018 Remi Collet <remi@remirepo.net> - 7.3.4-1
- update to 7.3.4

* Sun Sep  2 2018 Remi Collet <remi@remirepo.net> - 7.3.3-1
- update to 7.3.3

* Wed Aug 22 2018 Remi Collet <remi@remirepo.net> - 7.3.2-1
- update to 7.3.2

* Thu Aug  9 2018 Remi Collet <remi@remirepo.net> - 7.3.1-1
- update to 7.3.1

* Mon Jul 16 2018 Remi Collet <remi@remirepo.net> - 7.2.7-1
- update to 7.2.7
- allow phar-io/version 2.0

* Thu Jun 21 2018 Remi Collet <remi@remirepo.net> - 7.2.6-1
- update to 7.2.6

* Thu Jun 21 2018 Remi Collet <remi@remirepo.net> - 7.2.5-1
- update to 7.2.5
- raise dependency on phpunit/php-file-iterator 2.0.1

* Tue Jun  5 2018 Remi Collet <remi@remirepo.net> - 7.2.4-1
- update to 7.2.4

* Sun Jun  3 2018 Remi Collet <remi@remirepo.net> - 7.2.3-1
- update to 7.2.3

* Fri Jun  1 2018 Remi Collet <remi@remirepo.net> - 7.2.2-2
- manage php-doctrine-instantiator11

* Fri Jun  1 2018 Remi Collet <remi@remirepo.net> - 7.2.2-1
- update to 7.2.2
- raise dependency on phpunit/php-code-coverage 6.0.7

* Fri Jun  1 2018 Remi Collet <remi@remirepo.net> - 7.2.1-1
- update to 7.2.1

* Fri Jun  1 2018 Remi Collet <remi@remirepo.net> - 7.2.0-1
- update to 7.2.0
- add dependency on doctrine/instantiator 1.1
- raise dependency on myclabs/deep-copy 1.7
- raise dependency on phpunit/php-code-coverage 6.0.6
- raise dependency on phpunit/php-file-iterator 2.0
- phpunit/phpunit-mock-objects is merged
- open https://github.com/sebastianbergmann/phpunit/issues/3155
  TypeError: Return value of PHPUnit\Framework\TestCase::getStatus()...

* Wed May  2 2018 Remi Collet <remi@remirepo.net> - 7.1.5-1
- update to 7.1.5
- raise dependency on sebastian/comparator 3.0

* Wed Apr 18 2018 Remi Collet <remi@remirepo.net> - 7.1.4-1
- update to 7.1.4
- allow sebastian/comparator 3.0

* Mon Apr 16 2018 Remi Collet <remi@remirepo.net> - 7.1.3-1
- update to 7.1.3 (no change)
- raise dependency on phpunit/phpunit-mock-objects 6.1.1

* Tue Apr 10 2018 Remi Collet <remi@remirepo.net> - 7.1.2-1
- update to 7.1.2

* Mon Apr  9 2018 Remi Collet <remi@remirepo.net> - 7.1.1-1
- update to 7.1.1
- raise dependency on phpunit/phpunit-mock-objects 6.1

* Mon Mar 26 2018 Remi Collet <remi@remirepo.net> - 7.0.3-1
- update to 7.0.3
- raise dependency on phpunit/php-code-coverage 6.0.1

* Mon Feb 26 2018 Remi Collet <remi@remirepo.net> - 7.0.2-1
- Update to 7.0.2

* Tue Feb 13 2018 Remi Collet <remi@remirepo.net> - 7.0.1-1
- Update to 7.0.1

* Wed Feb  7 2018 Remi Collet <remi@remirepo.net> - 7.0.0-4
- fix weak dependency on php-phpunit-dbunit4

* Wed Feb  7 2018 Remi Collet <remi@remirepo.net> - 7.0.0-3
- re add undefine __brp_mangle_shebangs

* Tue Feb  6 2018 Remi Collet <remi@remirepo.net> - 7.0.0-2
- remove undefine __brp_mangle_shebangs for review #1541346

* Fri Feb  2 2018 Remi Collet <remi@remirepo.net> - 7.0.0-1
- Update to 7.0.0
- rename to phpunit7
- move to /usr/share/php/PHPUnit7
- raise dependency on PHP 7.1
- raise dependency on phpunit/php-code-coverage 6.0
- raise dependency on phpunit/php-timer 2.0
- raise dependency on phpunit/phpunit-mock-objects 6.0
- raise dependency on sebastian/diff 3.0
- raise dependency on phpunit/php-invoker 2.0
- use range dependencies on F27+
- use full path instead of relying on include_path

* Thu Feb  1 2018 Remi Collet <remi@remirepo.net> - 6.5.6-1
- Update to 6.5.6
- undefine __brp_mangle_shebangs
- use range dependencies on F27+

* Mon Dec 18 2017 Remi Collet <remi@remirepo.net> - 6.5.5-1
- Update to 6.5.5

* Mon Dec 11 2017 Remi Collet <remi@remirepo.net> - 6.5.4-1
- Update to 6.5.4
- raise dependency on phpunit/phpunit-mock-objects 5.0.5

* Thu Dec  7 2017 Remi Collet <remi@remirepo.net> - 6.5.3-1
- Update to 6.5.3
- raise dependency on phpunit/php-code-coverage 5.3

* Mon Dec  4 2017 Remi Collet <remi@remirepo.net> - 6.5.2-1
- Update to 6.5.2
- raise dependency on phpunit/phpunit-mock-objects 5.0.4

* Fri Dec  1 2017 Remi Collet <remi@remirepo.net> - 6.5.0-1
- Update to 6.5.0
- raise dependency on phpunit/php-code-coverage 5.2.3
- raise dependency on phpunit/php-file-iterator 1.4.3
- raise dependency on phpunit/phpunit-mock-objects 5.0

* Thu Nov  9 2017 Remi Collet <remi@remirepo.net> - 6.4.4-1
- Update to 6.4.4

* Tue Oct 17 2017 Remi Collet <remi@remirepo.net> - 6.4.3-1
- Update to 6.4.3

* Sun Oct 15 2017 Remi Collet <remi@remirepo.net> - 6.4.2-1
- Update to 6.4.2

* Sun Oct  8 2017 Remi Collet <remi@remirepo.net> - 6.4.1-1
- Update to 6.4.1

* Sun Sep 24 2017 Remi Collet <remi@remirepo.net> - 6.3.1-1
- Update to 6.3.1

* Mon Aug 21 2017 Remi Collet <remi@remirepo.net> - 6.3.0-2
- add optional dependency on php-phpunit-selenium

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 6.3.0-1
- Update to 6.3.0

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 6.2.4-1
- Update to 6.2.4

* Tue Jul  4 2017 Remi Collet <remi@remirepo.net> - 6.2.3-1
- Update to 6.2.3

* Tue Jun 13 2017 Remi Collet <remi@remirepo.net> - 6.2.2-1
- Update to 6.2.2

* Mon Jun  5 2017 Remi Collet <remi@remirepo.net> - 6.2.1-1
- Update to 6.2.1

* Mon May 22 2017 Remi Collet <remi@remirepo.net> - 6.1.4-1
- Update to 6.1.4 (no change)
- raise dependency on sebastian/diff 1.4.3 and allow v2
- raise dependency on sebastian/environment 3.0.2

* Sat Apr 29 2017 Remi Collet <remi@remirepo.net> - 6.1.3-1
- Update to 6.1.3
- raise dependency to only use sebastian/global-state v2

* Wed Apr 26 2017 Remi Collet <remi@remirepo.net> - 6.1.2-1
- Update to 6.1.2

* Sun Apr 23 2017 Remi Collet <remi@remirepo.net> - 6.1.1-1
- Update to 6.1.1
- raise dependency on phpunit/php-code-coverage >= 5.2
- raise dependency on sebastian/environment >= 3.0

* Fri Apr  7 2017 Remi Collet <remi@remirepo.net> - 6.1.0-1
- Update to 6.1.0
- add dependency on phar-io/manifest
- add dependency on phar-io/version
- raise dependency on sebastian/exporter 3.1

* Mon Apr  3 2017 Remi Collet <remi@remirepo.net> - 6.0.13-1
- Update to 6.0.13

* Thu Mar 30 2017 Remi Collet <remi@remirepo.net> - 6.0.11-2
- use fedora2 autoloader template

* Wed Mar 29 2017 Remi Collet <remi@remirepo.net> - 6.0.11-1
- Update to 6.0.11

* Mon Mar 20 2017 Remi Collet <remi@remirepo.net> - 6.0.10-1
- Update to 6.0.10

* Wed Mar 15 2017 Remi Collet <remi@remirepo.net> - 6.0.9-1
- Update to 6.0.9
- raise dependency on phpspec/prophecy 1.7
- raise dependency on sebastian/comparator 2.0
- raise dependency on sebastian/exporter 3.0
- raise dependency on sebastian/object-enumerator 3.0.2
- more explicit dependencies
- fix autoloader to only rely on include_path

* Fri Mar  3 2017 Remi Collet <remi@remirepo.net> - 6.0.8-2
- fix autoloader for dep. with multiple versions

* Thu Mar  2 2017 Remi Collet <remi@remirepo.net> - 6.0.8-1
- Update to 6.0.8

* Sun Feb 19 2017 Remi Collet <remi@fedoraproject.org> - 6.0.7-1
- update to 6.0.7

* Wed Feb  8 2017 Remi Collet <remi@fedoraproject.org> - 6.0.6-2
- cleanup autoloader (Symfony no more used)
- fix autoloader for dbunit
- fix description

* Wed Feb  8 2017 Remi Collet <remi@fedoraproject.org> - 6.0.6-1
- update to 6.0.6

* Tue Feb  7 2017 Remi Collet <remi@fedoraproject.org> - 6.0.5-1
- rename to phpunit6
- move to /usr/share/php/PHPUnit6
- raise dependency on phpunit/php-code-coverage 5.0.0
- raise dependency on phpunit/phpunit-mock-objects 4.0.0
- change spec license to CC-BY-SA

* Tue Feb  7 2017 Remi Collet <remi@fedoraproject.org> - 5.7.11-2
- add max version for some build dependencies
- only allow Symfony 2
- handle redirect to composer installed PHPUnit v6

* Sun Feb  5 2017 Remi Collet <remi@fedoraproject.org> - 5.7.11-1
- update to 5.7.11
- raise dependency on sebastian/comparator 1.2.4
- raise dependency on sebastian/global-state 1.1

* Sat Jan 28 2017 Remi Collet <remi@fedoraproject.org> - 5.7.9-1
- update to 5.7.9

* Fri Jan 27 2017 Remi Collet <remi@fedoraproject.org> - 5.7.8-2
- add upstream patch

* Thu Jan 26 2017 Remi Collet <remi@fedoraproject.org> - 5.7.8-1
- update to 5.7.8
- temporary ignore testNoTestCases

* Thu Jan 26 2017 Remi Collet <remi@fedoraproject.org> - 5.7.7-1
- update to 5.7.7

* Mon Jan 23 2017 Remi Collet <remi@fedoraproject.org> - 5.7.6-1
- update to 5.7.6

* Thu Dec 29 2016 Remi Collet <remi@fedoraproject.org> - 5.7.5-1
- update to 5.7.5

* Wed Dec 14 2016 Remi Collet <remi@fedoraproject.org> - 5.7.4-1
- update to 5.7.4

* Fri Dec  9 2016 Remi Collet <remi@fedoraproject.org> - 5.7.3-1
- update to 5.7.3
- raise dependency on phpspec/prophecy 1.6.2

* Sun Dec  4 2016 Remi Collet <remi@fedoraproject.org> - 5.7.2-1
- update to 5.7.2

* Fri Dec  2 2016 Remi Collet <remi@fedoraproject.org> - 5.7.1-1
- update to 5.7.1

* Fri Dec  2 2016 Remi Collet <remi@fedoraproject.org> - 5.7.0-1
- update to 5.7.0

* Mon Nov 28 2016 Remi Collet <remi@fedoraproject.org> - 5.6.7-1
- update to 5.6.7

* Tue Nov 22 2016 Remi Collet <remi@fedoraproject.org> - 5.6.5-1
- update to 5.6.5
- raise dependency on sebastian/comparator 1.2.2
- raise dependency on sebastian/exporter 2.0
- raise dependency on sebastian/object-enumerator 2.0

* Mon Nov 14 2016 Remi Collet <remi@fedoraproject.org> - 5.6.3-1
- update to 5.6.3

* Mon Oct 31 2016 Remi Collet <remi@fedoraproject.org> - 5.6.2-2
- fix autoloader (don't use symfony one for symfony components)

* Tue Oct 25 2016 Remi Collet <remi@fedoraproject.org> - 5.6.2-1
- update to 5.6.2 (no change)
- switch to fedora/autoloader

* Fri Oct  7 2016 Remi Collet <remi@fedoraproject.org> - 5.6.1-1
- update to 5.6.1

* Fri Oct  7 2016 Remi Collet <remi@fedoraproject.org> - 5.6.0-1
- update to 5.6.0
- drop dependency on php-tidy

* Mon Oct  3 2016 Remi Collet <remi@fedoraproject.org> - 5.5.7-1
- Update to 5.5.7 (no change)
- sources from github

* Mon Oct  3 2016 Remi Collet <remi@fedoraproject.org> - 5.5.6-1
- Update to 5.5.6
- sources from a git snapshot

* Wed Sep 21 2016 Remi Collet <remi@fedoraproject.org> - 5.5.5-1
- Update to 5.5.5

* Wed Aug 31 2016 Remi Collet <remi@fedoraproject.org> - 5.5.4-1
- Update to 5.5.4

* Fri Aug  5 2016 Remi Collet <remi@fedoraproject.org> - 5.5.0-1
- Update to 5.5.0

* Tue Jul 26 2016 Remi Collet <remi@fedoraproject.org> - 5.4.8-1
- Update to 5.4.8 (no change)
- raise dependency on phpunit/php-code-coverage >= 4.0.1

* Thu Jul 21 2016 Remi Collet <remi@fedoraproject.org> - 5.4.7-1
- Update to 5.4.7

* Thu Jun 16 2016 Remi Collet <remi@fedoraproject.org> - 5.4.6-1
- Update to 5.4.6 (no change)

* Wed Jun 15 2016 Remi Collet <remi@fedoraproject.org> - 5.4.5-1
- Update to 5.4.5

* Thu Jun  9 2016 Remi Collet <remi@fedoraproject.org> - 5.4.4-1
- Update to 5.4.4

* Fri Jun  3 2016 Remi Collet <remi@fedoraproject.org> - 5.4.2-1
- Update to 5.4.2

* Fri Jun  3 2016 Remi Collet <remi@fedoraproject.org> - 5.4.0-1
- Update to 5.4.0
- raise dependency on phpunit/php-code-coverage >= 4.0
- raise dependency on phpunit/phpunit-mock-objects >= 3.2

* Wed May 11 2016 Remi Collet <remi@fedoraproject.org> - 5.3.4-1
- Update to 5.3.4

* Wed Apr 13 2016 Remi Collet <remi@fedoraproject.org> - 5.3.2-1
- Update to 5.3.2

* Thu Apr  7 2016 Remi Collet <remi@fedoraproject.org> - 5.3.1-1
- Update to 5.3.1

* Fri Apr  1 2016 Remi Collet <remi@fedoraproject.org> - 5.3.0-1
- Update to 5.3.0
- add dependency on sebastian/object-enumerator
- raise dependency on phpunit/phpunit-mock-objects >= 3.1

* Tue Mar 15 2016 Remi Collet <remi@fedoraproject.org> - 5.2.12-1
- Update to 5.2.12

* Mon Mar 14 2016 Remi Collet <remi@fedoraproject.org> - 5.2.11-1
- Update to 5.2.11

* Thu Mar  3 2016 Remi Collet <remi@fedoraproject.org> - 5.2.10-1
- Update to 5.2.10
- raise dependency on phpunit/php-code-coverage >= 3.3.0

* Fri Feb 19 2016 Remi Collet <remi@fedoraproject.org> - 5.2.9-1
- Update to 5.2.9

* Thu Feb 18 2016 Remi Collet <remi@fedoraproject.org> - 5.2.8-1
- Update to 5.2.8
- raise dependency on phpunit/php-code-coverage >= 3.2.1

* Tue Feb 16 2016 Remi Collet <remi@fedoraproject.org> - 5.2.6-1
- Update to 5.2.6

* Sat Feb 13 2016 Remi Collet <remi@fedoraproject.org> - 5.2.5-1
- Update to 5.2.5
- raise dependency on phpunit/php-code-coverage >= 3.2

* Thu Feb 11 2016 Remi Collet <remi@fedoraproject.org> - 5.2.4-1
- Update to 5.2.4
- lower dependency on phpunit/php-code-coverage >= 3.0

* Sun Feb  7 2016 Remi Collet <remi@fedoraproject.org> - 5.2.2-1
- Update to 5.2.2

* Fri Feb  5 2016 Remi Collet <remi@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1

* Fri Feb  5 2016 Remi Collet <remi@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0
- raise dependency on phpunit/php-code-coverage >= 3.1

* Tue Feb  2 2016 Remi Collet <remi@fedoraproject.org> - 5.1.7-1
- Update to 5.1.7

* Fri Jan 29 2016 Remi Collet <remi@fedoraproject.org> - 5.1.6-1
- Update to 5.1.6

* Fri Jan 29 2016 Remi Collet <remi@fedoraproject.org> - 5.1.5-1
- Update to 5.1.5

* Mon Jan 11 2016 Remi Collet <remi@fedoraproject.org> - 5.1.4-1
- Update to 5.1.4

* Thu Dec 10 2015 Remi Collet <remi@fedoraproject.org> - 5.1.3-1
- Update to 5.1.3
- obsolete php-phpunit-PHPUnit-Selenium

* Mon Dec  7 2015 Remi Collet <remi@fedoraproject.org> - 5.1.2-1
- Update to 5.1.2

* Thu Dec  3 2015 Remi Collet <remi@fedoraproject.org> - 5.1.0-1
- Update to 5.1.0

* Mon Nov 30 2015 Remi Collet <remi@fedoraproject.org> - 5.0.10-1
- Update to 5.0.10
- run test suite with both PHP 5 and 7 when available

* Wed Nov 11 2015 Remi Collet <remi@fedoraproject.org> - 5.0.9-1
- Update to 5.0.9

* Fri Oct 23 2015 Remi Collet <remi@fedoraproject.org> - 5.0.8-1
- Update to 5.0.8 (no change)

* Thu Oct 22 2015 Remi Collet <remi@fedoraproject.org> - 5.0.7-1
- Update to 5.0.7

* Wed Oct 14 2015 Remi Collet <remi@fedoraproject.org> - 5.0.6-1
- Update to 5.0.6

* Mon Oct 12 2015 Remi Collet <remi@fedoraproject.org> - 5.0.5-1
- Update to 5.0.5

* Wed Oct  7 2015 Remi Collet <remi@fedoraproject.org> - 5.0.4-1
- Update to 5.0.4

* Fri Oct  2 2015 Remi Collet <remi@fedoraproject.org> - 5.0.3-1
- Update to 5.0.3 (no change)

* Fri Oct  2 2015 Remi Collet <remi@fedoraproject.org> - 5.0.2-1
- Update to 5.0.2

* Tue Sep 29 2015 Remi Collet <remi@fedoraproject.org> - 5.0.0-0.1.20150927gite3b3f36
- update to 5.0.0-dev
- raise dependency on PHP >= 5.6
- raise dependency on phpunit/php-code-coverage ~3.0
- raise dependency on phpunit/phpunit-mock-objects ~3.0
- add dependency on sebastian/resource-operations ~1.0
- add dependency on myclabs/deep-copy ~1.3

* Sun Sep 27 2015 Remi Collet <remi@fedoraproject.org> - 4.8.9-2
- add --atleast-version command option, backported from 5.0

* Mon Sep 21 2015 Remi Collet <remi@fedoraproject.org> - 4.8.9-1
- Update to 4.8.9

* Sun Sep 20 2015 Remi Collet <remi@fedoraproject.org> - 4.8.8-1
- Update to 4.8.8

* Mon Sep 14 2015 Remi Collet <remi@fedoraproject.org> - 4.8.7-1
- Update to 4.8.7 (no change)

* Tue Aug 25 2015 Remi Collet <remi@fedoraproject.org> - 4.8.6-1
- Update to 4.8.6

* Fri Aug 21 2015 Remi Collet <remi@fedoraproject.org> - 4.8.5-1
- Update to 4.8.5 (no change)

* Sat Aug 15 2015 Remi Collet <remi@fedoraproject.org> - 4.8.4-1
- Update to 4.8.4

* Mon Aug 10 2015 Remi Collet <remi@fedoraproject.org> - 4.8.3-1
- Update to 4.8.3

* Fri Aug  7 2015 Remi Collet <remi@fedoraproject.org> - 4.8.2-1
- Update to 4.8.2

* Fri Aug  7 2015 Remi Collet <remi@fedoraproject.org> - 4.8.1-1
- Update to 4.8.1 (no change)

* Fri Aug  7 2015 Remi Collet <remi@fedoraproject.org> - 4.8.0-1
- Update to 4.8.0
- raise dependency on sebastian/environment 1.3
- rely on include_path for all dependencies
- add Changelog in documentation

* Mon Jul 13 2015 Remi Collet <remi@fedoraproject.org> - 4.7.7-1
- Update to 4.7.7 (no change)

* Tue Jun 30 2015 Remi Collet <remi@fedoraproject.org> - 4.7.6-1
- Update to 4.7.6

* Tue Jun 30 2015 Remi Collet <remi@fedoraproject.org> - 4.7.5-2
- use $fedoraClassLoader autoloader

* Sun Jun 21 2015 Remi Collet <remi@fedoraproject.org> - 4.7.5-1
- Update to 4.7.5

* Thu Jun 18 2015 Remi Collet <remi@fedoraproject.org> - 4.7.4-1
- Update to 4.7.4
- raise dependency on phpunit/php-timer >= 1.0.6

* Thu Jun 11 2015 Remi Collet <remi@fedoraproject.org> - 4.7.3-1
- Update to 4.7.3

* Sun Jun  7 2015 Remi Collet <remi@fedoraproject.org> - 4.7.2-1
- Update to 4.7.2

* Fri Jun  5 2015 Remi Collet <remi@fedoraproject.org> - 4.7.1-1
- Update to 4.7.1
- raise dependency on phpunit/php-code-coverage ~2.1
- improve autoloader

* Wed Jun  3 2015 Remi Collet <remi@fedoraproject.org> - 4.6.10-1
- Update to 4.6.10

* Fri May 29 2015 Remi Collet <remi@fedoraproject.org> - 4.6.9-1
- Update to 4.6.9

* Thu May 28 2015 Remi Collet <remi@fedoraproject.org> - 4.6.8-1
- Update to 4.6.8 (no change)

* Tue May 26 2015 Remi Collet <remi@fedoraproject.org> - 4.6.7-3
- ensure compatibility with SCL

* Tue May 26 2015 Remi Collet <remi@fedoraproject.org> - 4.6.7-2
- detect and redirect to composer installed version #1157910

* Mon May 25 2015 Remi Collet <remi@fedoraproject.org> - 4.6.7-1
- Update to 4.6.7 (no change)

* Thu Apr 30 2015 Remi Collet <remi@fedoraproject.org> - 4.6.6-1
- Update to 4.6.6

* Wed Apr 29 2015 Remi Collet <remi@fedoraproject.org> - 4.6.5-1
- Update to 4.6.5

* Fri Apr 17 2015 Remi Collet <remi@fedoraproject.org> - 4.6.4-2
- keep upstream shebang with /usr/bin/env (for SCL)

* Mon Apr 13 2015 Remi Collet <remi@fedoraproject.org> - 4.6.4-1
- Update to 4.6.4

* Tue Apr  7 2015 Remi Collet <remi@fedoraproject.org> - 4.6.2-1
- Update to 4.6.2

* Fri Apr  3 2015 Remi Collet <remi@fedoraproject.org> - 4.6.1-1
- Update to 4.6.1

* Fri Apr  3 2015 Remi Collet <remi@fedoraproject.org> - 4.6.0-1
- Update to 4.6.0
- raise dependencies on file-iterator 1.4 and diff 1.2

* Sun Mar 29 2015 Remi Collet <remi@fedoraproject.org> - 4.5.1-1
- Update to 4.5.1

* Fri Feb 13 2015 Remi Collet <remi@fedoraproject.org> - 4.5.0-1
- Update to 4.5.0
- add dependency on phpspec/prophecy
- raise dependencies on sebastian/comparator >= 1.1,
  sebastian/environment >= 1.2, sebastian/exporter >= 1.2
  and doctrine/instantiator >= 1.0.4 (for autoloader file)

* Tue Jan 27 2015 Remi Collet <remi@fedoraproject.org> - 4.4.5-1
- Update to 4.4.5 (no change)

* Tue Jan 27 2015 Remi Collet <remi@fedoraproject.org> - 4.4.4-2
- add dependency on sebastian/recursion-context

* Sun Jan 25 2015 Remi Collet <remi@fedoraproject.org> - 4.4.4-1
- Update to 4.4.4

* Sun Jan 18 2015 Remi Collet <remi@fedoraproject.org> - 4.4.2-1
- Update to 4.4.2

* Sun Dec 28 2014 Remi Collet <remi@fedoraproject.org> - 4.4.1-1
- Update to 4.4.1

* Fri Dec  5 2014 Remi Collet <remi@fedoraproject.org> - 4.4.0-1
- Update to 4.4.0
- add dependency on sebastian/global-state

* Tue Nov 11 2014 Remi Collet <remi@fedoraproject.org> - 4.3.5-1
- Update to 4.3.5
- define date.timezone in phpunit command to avoid warning

* Sat Oct 25 2014 Remi Collet <remi@fedoraproject.org> - 4.3.4-1
- Update to 4.3.4
- raise dependency on phpunit/php-file-iterator >= 1.3.2

* Fri Oct 17 2014 Remi Collet <remi@fedoraproject.org> - 4.3.3-1
- Update to 4.3.3

* Thu Oct 16 2014 Remi Collet <remi@fedoraproject.org> - 4.3.2-1
- Update to 4.3.2

* Wed Oct  8 2014 Remi Collet <remi@fedoraproject.org> - 4.3.1-2
- new upstream patch for "no colors" patch
- raise dependency on sebastian/environment >= 1.1

* Mon Oct  6 2014 Remi Collet <remi@fedoraproject.org> - 4.3.1-1
- Update to 4.3.1 (no change)

* Mon Oct  6 2014 Remi Collet <remi@fedoraproject.org> - 4.3.0-2
- only enable colors when output to a terminal (from 4.4)
- open https://github.com/sebastianbergmann/phpunit/pull/1458

* Fri Oct  3 2014 Remi Collet <remi@fedoraproject.org> - 4.3.0-1
- Update to 4.3.0
- drop dependencies on ocramius/instantiator and ocramius/lazy-map
- add dependency on doctrine/instantiator
- raise dependency on phpunit/phpunit-mock-objects >= 2.3

* Sun Sep 14 2014 Remi Collet <remi@fedoraproject.org> - 4.2.6-1
- Update to 4.2.6 (no change)

* Sun Sep  7 2014 Remi Collet <remi@fedoraproject.org> - 4.2.5-1
- Update to 4.2.5 (no change)

* Sun Aug 31 2014 Remi Collet <remi@fedoraproject.org> - 4.2.4-1
- Update to 4.2.4

* Thu Aug 28 2014 Remi Collet <remi@fedoraproject.org> - 4.2.3-1
- Update to 4.2.3

* Mon Aug 18 2014 Remi Collet <remi@fedoraproject.org> - 4.2.2-1
- Update to 4.2.2

* Sun Aug 17 2014 Remi Collet <remi@fedoraproject.org> - 4.2.1-1
- Update to 4.2.1

* Mon Aug 11 2014 Remi Collet <remi@fedoraproject.org> - 4.2.0-1
- Update to 4.2.0
- raise dependency on phpunit/phpunit-mock-objects >= 2.2
- add dependency on ocramius/instantiator, ocramius/lazy-map
  and symfony/class-loader

* Fri Jul 18 2014 Remi Collet <remi@fedoraproject.org> - 4.1.4-1
- Update to 4.1.4
- composer dependencies
- add missing documentation and license

* Fri Jun 13 2014 Remi Collet <remi@fedoraproject.org> - 4.1.3-1
- Update to 4.1.3

* Sat Jun  7 2014 Remi Collet <remi@fedoraproject.org> - 4.1.2-1
- Update to 4.1.2 (no change)
- improve test suite bootstraping
- add composer provide

* Mon May 26 2014 Remi Collet <remi@fedoraproject.org> - 4.1.1-1
- Update to 4.1.1

* Tue May  6 2014 Remi Collet <remi@fedoraproject.org> - 4.1.0-2
- fix some autoload issues

* Sat May  3 2014 Remi Collet <remi@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 4.0.18-2
- cleanup pear registry

* Tue Apr 29 2014 Remi Collet <remi@fedoraproject.org> - 4.0.18-1
- update to 4.0.18
- sources from github

* Tue Apr 22 2014 Remi Collet <remi@fedoraproject.org> - 3.7.35-2
- remove message about deprecated PEAR channel

* Tue Apr 22 2014 Remi Collet <remi@fedoraproject.org> - 3.7.35-1
- Update to 3.7.35

* Sun Apr 06 2014 Remi Collet <remi@fedoraproject.org> - 3.7.34-1
- Update to 3.7.34

* Tue Feb 25 2014 Remi Collet <remi@fedoraproject.org> - 3.7.32-1
- Update to 3.7.32 (no change)

* Mon Feb 03 2014 Remi Collet <remi@fedoraproject.org> - 3.7.31-1
- Update to 3.7.31 (no change)

* Fri Jan 31 2014 Remi Collet <remi@fedoraproject.org> - 3.7.30-1
- Update to 3.7.30

* Wed Jan 15 2014 Remi Collet <remi@fedoraproject.org> - 3.7.29-1
- Update to 3.7.29 (stable)

* Thu Oct 17 2013 Remi Collet <remi@fedoraproject.org> - 3.7.28-1
- Update to 3.7.28
- add Spec license header
- open https://github.com/sebastianbergmann/phpunit/issues/1029

* Mon Sep 16 2013 Remi Collet <remi@fedoraproject.org> - 3.7.27-1
- Update to 3.7.27 (no change)

* Fri Sep 13 2013 Remi Collet <remi@fedoraproject.org> - 3.7.26-1
- Update to 3.7.26 (no change)

* Tue Sep 10 2013 Remi Collet <remi@fedoraproject.org> - 3.7.25-1
- Update to 3.7.25 (no change)

* Tue Aug 20 2013 Remi Collet <remi@fedoraproject.org> - 3.7.24-1
- Update to 3.7.24

* Mon Aug 05 2013 Remi Collet <remi@fedoraproject.org> - 3.7.23-1
- Update to 3.7.23
- raise dependency on phpunit/PHP_Timer 1.0.4

* Mon Jul 08 2013 Remi Collet <remi@fedoraproject.org> - 3.7.22-1
- Update to 3.7.22

* Fri May 24 2013 Remi Collet <remi@fedoraproject.org> - 3.7.21-1
- Update to 3.7.21

* Mon May 13 2013 Remi Collet <remi@fedoraproject.org> - 3.7.20-1
- Update to 3.7.20

* Mon Mar 25 2013 Remi Collet <remi@fedoraproject.org> - 3.7.19-1
- Update to 3.7.19
- requires pear.symfony.com/Yaml >= 2.0.0, <= 2.2.99

* Fri Mar 08 2013 Remi Collet <remi@fedoraproject.org> - 3.7.18-1
- Update to 3.7.18

* Thu Mar 07 2013 Remi Collet <remi@fedoraproject.org> - 3.7.17-1
- Update to 3.7.17

* Wed Mar 06 2013 Remi Collet <remi@fedoraproject.org> - 3.7.16-1
- Update to 3.7.16

* Tue Mar 05 2013 Remi Collet <remi@fedoraproject.org> - 3.7.15-1
- Update to 3.7.15

* Thu Feb 14 2013 Remi Collet <remi@fedoraproject.org> - 3.7.14-1
- Update to 3.7.14

* Sun Jan 13 2013 Remi Collet <remi@fedoraproject.org> - 3.7.13-1
- Version 3.7.13 (stable) - API 3.7.0 (stable)

* Thu Jan 10 2013 Remi Collet <remi@fedoraproject.org> - 3.7.12-1
- Version 3.7.12 (stable) - API 3.7.0 (stable)

* Wed Jan  9 2013 Remi Collet <remi@fedoraproject.org> - 3.7.11-1
- Version 3.7.11 (stable) - API 3.7.0 (stable)

* Sun Dec  2 2012 Remi Collet <remi@fedoraproject.org> - 3.7.10-1
- Version 3.7.10 (stable) - API 3.7.0 (stable)

* Wed Nov 07 2012 Remi Collet <remi@fedoraproject.org> - 3.7.9-1
- Version 3.7.9 (stable) - API 3.7.0 (stable)

* Thu Oct 18 2012 Remi Collet <remi@fedoraproject.org> - 3.7.8-1
- Version 3.7.8 (stable) - API 3.7.0 (stable)

* Thu Oct 11 2012 Remi Collet <remi@fedoraproject.org> - 3.7.7-1
- Version 3.7.7 (stable) - API 3.7.0 (stable)

* Sun Oct  7 2012 Remi Collet <remi@fedoraproject.org> - 3.7.6-1
- Version 3.7.6 (stable) - API 3.7.0 (stable)

* Sat Oct  6 2012 Remi Collet <remi@fedoraproject.org> - 3.7.5-1
- Version 3.7.5 (stable) - API 3.7.0 (stable)

* Sat Oct  6 2012 Remi Collet <remi@fedoraproject.org> - 3.7.4-1
- Version 3.7.4 (stable) - API 3.7.0 (stable)
- add Conflicts for max version of PHP_CodeCoverage and PHPUnit_MockObject

* Thu Sep 20 2012 Remi Collet <remi@fedoraproject.org> - 3.7.1-1
- Version 3.7.1 (stable) - API 3.7.0 (stable)
- raise dependencies: php 5.3.3, PHP_CodeCoverage 1.2.1,
  PHP_Timer 1.0.2, Yaml 2.1.0 (instead of YAML from symfony 1)

* Sat Aug 04 2012 Remi Collet <remi@fedoraproject.org> - 3.6.12-1
- Version 3.6.12 (stable) - API 3.6.0 (stable)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Remi Collet <remi@fedoraproject.org> - 3.6.11-1
- Version 3.6.11 (stable) - API 3.6.0 (stable)

* Fri Jan 27 2012 Remi Collet <remi@fedoraproject.org> - 3.6.10-1
- Version 3.6.10 (stable) - API 3.6.0 (stable)
- raise PHP_Invokers >= 1.1.0

* Tue Jan 24 2012 Remi Collet <remi@fedoraproject.org> - 3.6.9-1
- Version 3.6.9 (stable) - API 3.6.0 (stable)

* Sat Jan 21 2012 Remi Collet <remi@fedoraproject.org> - 3.6.8-1
- Version 3.6.8 (stable) - API 3.6.0 (stable)

* Thu Jan 05 2012 Remi Collet <remi@fedoraproject.org> - 3.6.7-1
- Version 3.6.7 (stable) - API 3.6.0 (stable)

* Mon Jan 02 2012 Remi Collet <remi@fedoraproject.org> - 3.6.6-1
- Version 3.6.6 (stable) - API 3.6.0 (stable)

* Mon Dec 19 2011 Remi Collet <remi@fedoraproject.org> - 3.6.5-1
- Version 3.6.5 (stable) - API 3.6.0 (stable)

* Sat Nov 26 2011 Remi Collet <remi@fedoraproject.org> - 3.6.4-1
- Version 3.6.4 (stable) - API 3.6.0 (stable)

* Fri Nov 11 2011 Remi Collet <remi@fedoraproject.org> - 3.6.3-1
- Version 3.6.3 (stable) - API 3.6.0 (stable)

* Fri Nov 04 2011 Remi Collet <remi@fedoraproject.org> - 3.6.2-1
- Version 3.6.2 (stable) - API 3.6.0 (stable)

* Tue Nov 01 2011 Remi Collet <remi@fedoraproject.org> - 3.6.0-1
- Version 3.6.0 (stable) - API 3.6.0 (stable)

* Fri Aug 19 2011 Remi Collet <remi@fedoraproject.org> - 3.5.15-1
- Version 3.5.15 (stable) - API 3.5.7 (stable)
- raise PEAR dependency to 1.9.3

* Fri Jun 10 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.14-1
- Version 3.5.14 (stable) - API 3.5.7 (stable)

* Tue May  3 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.13-2
- rebuild for doc in /usr/share/doc/pear

* Tue Mar  8 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.13-1
- Version 3.5.13 (stable) - API 3.5.7 (stable)
- remove PEAR hack (only needed for EPEL)
- raise PEAR dependency to 1.9.2
- remove duplicate dependency (YAML)

* Thu Feb 24 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.12-1
- Version 3.5.12 (stable) - API 3.5.7 (stable)

* Wed Feb 16 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.11-1
- Version 3.5.11 (stable) - API 3.5.7 (stable)
- new dependency on php-pear(XML_RPC2)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.10-1
- Version 3.5.10 (stable) - API 3.5.7 (stable)

* Tue Jan 18 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.9-1
- Version 3.5.9 (stable) - API 3.5.7 (stable)

* Tue Jan 11 2011 Remi Collet <Fedora@famillecollet.com> - 3.5.7-1
- Version 3.5.7 (stable) - API 3.5.7 (stable)
- README, CHANGELOG and LICENSE are now in the tarball

* Mon Dec 20 2010 Remi Collet <Fedora@famillecollet.com> - 3.5.6-1
- Version 3.5.6 (stable) - API 3.5.4 (stable)
- move README.mardown to README (was Changelog, now links to doc)
- add CHANGELOG
- not more doc provided by upstream

* Mon Nov 22 2010 Remi Collet <Fedora@famillecollet.com> - 3.5.5-1
- Version 3.5.5 (stable) - API 3.5.4 (stable)

* Wed Nov 17 2010 Remi Collet <Fedora@famillecollet.com> - 3.5.4-1
- Version 3.5.4 (stable) - API 3.5.4 (stable)

* Wed Oct 27 2010 Remi Collet <Fedora@famillecollet.com> - 3.5.3-1
- Update to 3.5.3
- new requires and new packages for extensions of PHPUnit
  PHPUnit_MockObject, PHPUnit_Selenium, DbUnit
- lower PEAR dependency to allow el6 build
- define timezone during build

* Thu Jul 22 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.15-1
- Update to 3.4.15

* Sat Jun 19 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.14-1
- Update to 3.4.14

* Sat May 22 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.13-1
- Update to 3.4.13
- add README.markdown (Changelog)

* Wed Apr 07 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.12-1
- Update to 3.4.12

* Thu Feb 18 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.11-1.1
- Update to 3.4.11

* Wed Feb 10 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.10-1
- Update to 3.4.10

* Sun Jan 24 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.9-1
- Update to 3.4.9

* Sat Jan 16 2010 Remi Collet <Fedora@famillecollet.com> - 3.4.7-1
- Update to 3.4.7
- rename from php-pear-PHPUnit to php-phpunit-PHPUnit
- update dependencies (PEAR 1.8.1, YAML, php-soap)

* Sat Sep 12 2009 Christopher Stone <chris.stone@gmail.com> 3.3.17-1
- Upstream sync

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 02 2009 Remi Collet <Fedora@famillecollet.com> - 3.3.16-1
- Upstream sync
- Fix requires (remove hint) and raise PEAR version to 1.7.1
- rename %%{pear_name}.xml to %%{name}.xml

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov  8 2008 Christopher Stone <chris.stone@gmail.com> 3.3.4-1
- Upstream sync

* Thu Oct 23 2008 Christopher Stone <chris.stone@gmail.com> 3.3.2-1
- Upstream sync
- Remove no longer needed Obsolete/Provides

* Thu Oct 09 2008 Christopher Stone <chris.stone@gmail.com> 3.3.1-1
- Upstream sync

* Thu Oct 09 2008 Christopher Stone <chris.stone@gmail.com> 3.2.21-1
- Upstream sync
- Add php-xml to Requires (bz #464758)

* Thu May 22 2008 Christopher Stone <chris.stone@gmail.com> 3.2.19-1
- Upstream sync

* Thu Feb 21 2008 Christopher Stone <chris.stone@gmail.com> 3.2.15-1
- Upstream sync

* Wed Feb 13 2008 Christopher Stone <chris.stone@gmail.com> 3.2.13-1
- Upstream sync

* Sun Nov 25 2007 Christopher Stone <chris.stone@gmail.com> 3.2.1-1
- Upstream sync

* Sat Sep 08 2007 Christopher Stone <chris.stone@gmail.com> 3.1.8-1
- Upstream sync

* Sun May 06 2007 Christopher Stone <chris.stone@gmail.com> 3.0.6-1
- Upstream sync

* Thu Mar 08 2007 Christopher Stone <chris.stone@gmail.com> 3.0.5-3
- Fix testdir
- Fix Provides version

* Wed Mar 07 2007 Christopher Stone <chris.stone@gmail.com> 3.0.5-2
- Add Obsoletes/Provides for php-pear(PHPUnit2)
- Requires php-pear(PEAR) >= 1.5.0
- Own %%{pear_testdir}/%%{pear_name}
- Remove no longer needed manual channel install
- Simplify %%doc
- Only unregister old phpunit on upgrade

* Mon Feb 26 2007 Christopher Stone <chris.stone@gmail.com> 3.0.5-1
- Upstream sync

* Wed Feb 21 2007 Christohper Stone <chris.stone@gmail.com> 3.0.4-1
- Upstream sync

* Mon Jan 29 2007 Christopher Stone <chris.stone@gmail.com> 3.0.3-1
- Upstream sync

* Sun Jan 14 2007 Christopher Stone <chris.stone@gmail.com> 3.0.2-1
- Upstream sync

* Fri Jan 05 2007 Christopher Stone <chris.stone@gmail.com> 3.0.1-1
- Upstream sync

* Wed Dec 27 2006 Christopher Stone <chris.stone@gmail.com> 3.0.0-1
- Initial Release