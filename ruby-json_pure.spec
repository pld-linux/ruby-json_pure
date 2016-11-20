#
# Conditional build:
%bcond_with	tests		# build without tests

%define pkgname json_pure
Summary:	JSON Implementation for Ruby
Name:		ruby-%{pkgname}
Version:	1.8.1
Release:	1
Group:		Development/Languages
# TODO: License should be probably updated.
# https://github.com/flori/json/issues/213
License:	GPLv2 or Ruby
Source0:	http://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	951f69022d98656b516b77bb8a98c605
URL:		http://flori.github.com/json
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	ruby-test-unit
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a JSON implementation in pure Ruby.

%prep
%setup -q -n %{pkgname}-%{version}

rm lib/json/ext/.keep

%build
# write .gemspec
%__gem_helper spec

%if %{with tests}
JSON=pure ruby -e 'Dir.glob "./tests/**/test_*.rb", &method(:require)'
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README-json-jruby.markdown README.rdoc COPYING-json-jruby COPYING CHANGES VERSION TODO
%{ruby_vendorlibdir}/json.rb
%{ruby_vendorlibdir}/json
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
