Summary:	Marios Hadjieleftheriou's tools library
Summary(pl.UTF-8):	Biblioteka narzędziowa Mariosa Hadjieleftheriou
Name:		mh-tools
Version:	0.54b
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://research.att.com/~marioh/tools/tools.054b.tar.bz2
# Source0-md5:	c5844269eca9232f7833801e9d61f8cb
URL:		http://research.att.com/~marioh/tools/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a useful collection of utility classes for C++. Contains
random number generators (mersenne), hash functions (universal hashing
and SHA1), an RLE compressor, architecture detection functions, string
tokenizers, and other useful stuff.

%description -l pl.UTF-8
Ten pakiet to przydatny zbiór klas narzędziowych dla C++. Zawiera
generatory liczb losowych (mersenne), funkcje haszujące (haszowanie
uniwersalne i SHA1), kompresor RLE, funcke wykrywajace architekturę,
tokenizery łańcuchów znaków i inne przydatne elementy.

%package devel
Summary:	Header files for Marios Hadjieleftheriou's tools library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki narzędziowej Mariosa Hadjieleftheriou
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Marios Hadjieleftheriou's tools library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki narzędziowej Mariosa Hadjieleftheriou.

%package static
Summary:	Static version of Marios Hadjieleftheriou's tools library
Summary(pl.UTF-8):	Statyczna wersja biblioteki narzędziowej Mariosa Hadjieleftheriou
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of Marios Hadjieleftheriou's tools library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki narzędziowej Mariosa Hadjieleftheriou.

%prep
%setup -q -n tools

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/tools

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
