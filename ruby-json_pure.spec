%define pkgname json_pure
Summary:	JSON implementation in pure Ruby
Name:		ruby-%{pkgname}
Version:	2.8.1
Release:	1
License:	Ruby
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	ae7922ccef92cc0a02dcb56d9b3dd23b
URL:		https://ruby.github.io/json
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a JSON implementation in pure Ruby.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec
%{__sed} -i -e 's/s.version = .*/s.version = "%{version}"/' %{pkgname}.gemspec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md README.md
%{ruby_vendorlibdir}/json
%{ruby_specdir}/%{pkgname}.gemspec
