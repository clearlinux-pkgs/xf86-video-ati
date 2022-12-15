#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x5A81AF8E6ADBB200 (daenzer@debian.org)
#
Name     : xf86-video-ati
Version  : 19.1.0
Release  : 151
URL      : https://www.x.org/releases/individual/driver/xf86-video-ati-19.1.0.tar.gz
Source0  : https://www.x.org/releases/individual/driver/xf86-video-ati-19.1.0.tar.gz
Source1  : https://www.x.org/releases/individual/driver/xf86-video-ati-19.1.0.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: xf86-video-ati-data = %{version}-%{release}
Requires: xf86-video-ati-lib = %{version}-%{release}
Requires: xf86-video-ati-license = %{version}-%{release}
Requires: xf86-video-ati-man = %{version}-%{release}
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libdrm_radeon)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xf86driproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)
Patch1: backport-gcc10.patch

%description
xf86-video-ati - ATI/AMD Radeon video driver for the Xorg X server
------------------------------------------------------------------

%package data
Summary: data components for the xf86-video-ati package.
Group: Data

%description data
data components for the xf86-video-ati package.


%package lib
Summary: lib components for the xf86-video-ati package.
Group: Libraries
Requires: xf86-video-ati-data = %{version}-%{release}
Requires: xf86-video-ati-license = %{version}-%{release}

%description lib
lib components for the xf86-video-ati package.


%package license
Summary: license components for the xf86-video-ati package.
Group: Default

%description license
license components for the xf86-video-ati package.


%package man
Summary: man components for the xf86-video-ati package.
Group: Default

%description man
man components for the xf86-video-ati package.


%prep
%setup -q -n xf86-video-ati-19.1.0
cd %{_builddir}/xf86-video-ati-19.1.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609782072
export GCC_IGNORE_WERROR=1
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1609782072
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-video-ati
cp %{_builddir}/xf86-video-ati-19.1.0/COPYING %{buildroot}/usr/share/package-licenses/xf86-video-ati/a297a2b3d9f367ccee795c8a4260d8c7f40ab78f
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/X11/xorg.conf.d/10-radeon.conf

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/drivers/ati_drv.so
/usr/lib64/xorg/modules/drivers/radeon_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-video-ati/a297a2b3d9f367ccee795c8a4260d8c7f40ab78f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man4/ati.4
/usr/share/man/man4/radeon.4
