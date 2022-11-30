%define debug_package		%{nil}

Summary:	Neofetch is a CLI system information tool written in BASH
Name:		neofetch
Version:	7.1.0.2
Release:	1
License:	MIT
Group:		Shells
Url:		https://github.com/dylanaraps/neofetch
#Source0:	https://github.com/dylanaraps/neofetch/archive/%{version}/%{name}-%{version}.tar.gz
Source:%{name}-%version.tar.gz
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
