%define staticname	%mklibname nacl -d -s

Name:		nacl
Summary:	Networking and Cryptography library
Version:	20110221
Release:	1
License:	Public Domain
Group:		System/Libraries
URL:		http://nacl.cr.yp.to/
Source0:	http://hyperelliptic.org/nacl/%{name}-%{version}.tar.bz2

%description
NaCl (pronounced "salt") is a new easy-to-use high-speed software library
for network communication, encryption, decryption, signatures, etc. NaCl's goal
is to provide all of the core operations needed to build higher-level
cryptographic tools.

%package -n %{staticname}
Summary:	NaCl library for static linking
Provides:	%{name}-static-devel = %{EVRD}

%description -n %{staticname}
NaCl (pronounced "salt") is a new easy-to-use high-speed software library
for network communication, encryption, decryption, signatures, etc. NaCl's goal
is to provide all of the core operations needed to build higher-level
cryptographic tools.

%prep
%setup -q

%build
%setup_compile_flags
./do

%install
SHORTHOSTNAME=$(echo $HOSTNAME | cut -d. -f1 | sed 's/-//g')
%ifarch x86_64
mv build/${SHORTHOSTNAME}/include/amd64/* build/${SHORTHOSTNAME}/include/
%else
%ifarch %{ix86}
mv build/${SHORTHOSTNAME}/include/x86/* build/${SHORTHOSTNAME}/include/
%endif
%endif
mkdir build/${SHORTHOSTNAME}/include/nacl
mv build/${SHORTHOSTNAME}/include/*.h build/${SHORTHOSTNAME}/include/nacl/
%ifarch x86_64
mv build/${SHORTHOSTNAME}/lib/amd64/* build/${SHORTHOSTNAME}/lib/
%else
%ifarch %{ix86}
mv build/${SHORTHOSTNAME}/lib/x86/* build/${SHORTHOSTNAME}/lib/
%endif
%endif
rm -rf build/${SHORTHOSTNAME}/log
rm -rf build/${SHORTHOSTNAME}/work
rm -rf build/${SHORTHOSTNAME}/data
rm -rf build/${SHORTHOSTNAME}/include/x86
rm -rf build/${SHORTHOSTNAME}/include/amd64
rm -rf build/${SHORTHOSTNAME}/include/lpia
rm -rf build/${SHORTHOSTNAME}/lib/x86
rm -rf build/${SHORTHOSTNAME}/lib/amd64
rm -rf build/${SHORTHOSTNAME}/lib/lpia
rm -f build/${SHORTHOSTNAME}/bin/ok*
rm -f build/${SHORTHOSTNAME}/lib/*.o
rm build/${SHORTHOSTNAME}/include/nacl/cpuid.h

mkdir -p %{buildroot}%{_prefix}
mv build/$SHORTHOSTNAME/include %{buildroot}%{_includedir}
mv build/$SHORTHOSTNAME/bin %{buildroot}%{_bindir}
mv build/$SHORTHOSTNAME/lib %{buildroot}%{_libdir}

%files
%{_bindir}/*

%files -n %{staticname}
%{_includedir}/nacl/
%{_libdir}/libnacl.a


%changelog
* Mon Apr 02 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 20110221-1
+ Revision: 788837
- imported package nacl

