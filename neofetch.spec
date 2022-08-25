%define debug_package		%{nil}

Summary:	Neofetch is a CLI system information tool written in BASH
Name:		neofetch
Version:	7.1.0.1
Release:	1
License:	MIT
Group:		Shells
Url:		https://github.com/dylanaraps/neofetch
#Source0:	https://github.com/dylanaraps/neofetch/archive/%{version}/%{name}-%{version}.tar.gz
Source:%{name}-%version.tar.gz
# This patch add support for OpenMandriva Lx. More https://github.com/dylanaraps/neofetch/issues/1116 (penguin)
# Merged in upstream. So disable it for now.
#Patch0:   openmandriva-support.patch
BuildArch: 	noarch

%description
Neofetch is a CLI system information tool written in BASH. 
Neofetch displays information about your system next to an 
image, your OS logo, or any ascii file of your choice. 

%prep
%setup -q
%autopatch -p1

%build
%make_build

%install
%make_install

%files
%doc README.md LICENSE.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
