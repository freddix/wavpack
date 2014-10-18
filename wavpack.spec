Summary:	Open audio compression codec
Name:		wavpack
Version:	4.70.0
Release:	1
License:	other
Group:		Libraries
Source0:	http://www.wavpack.com/%{name}-%{version}.tar.bz2
# Source0-md5:	4c0186ef0dc8367ce5cd7cc0f398b714
URL:		http://www.wavpack.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WavPack is a completely open audio compression format providing
lossless, high-quality lossy, and a unique hybrid compression mode.

%package libs
Summary:	Wavpack library
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs
Wavpack library.

%package devel
Summary:	Header files for Wavpack
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for Wavpack.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/wavpack.1*
%{_mandir}/man1/wvgain.1*
%{_mandir}/man1/wvunpack.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/wavpack
%{_pkgconfigdir}/*.pc

