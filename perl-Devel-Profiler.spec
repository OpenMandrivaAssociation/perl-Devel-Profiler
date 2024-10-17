%define upstream_name    Devel-Profiler
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:    A Perl profiler compatible with dprofpp  
License:	GPL+ and Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/S/SA/SAMTREGAR/Devel-Profiler-%{upstream_version}.tar.bz2

# needed for dprofpp
BuildRequires: perl-devel
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module implements a Perl profiler that outputs profiling data in
a format compatible with "dprofpp", Devel::DProf's profile analysis
tool.  It is meant to be a drop-in replacement for Devel::DProf.

NOTE: If Devel::DProf works for your application then there is no
reason to use this module.


%prep
%setup -q -n Devel-Profiler-%{upstream_version}
# broken http://rt.cpan.org/Public/Bug/Display.html?id=7400
rm -f t/01basic.t 
# broken due to 5.10 - http://rt.cpan.org/Public/Bug/Display.html?id=34214
rm -f t/07constants.t  t/09fcntl.t 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 653408
- rebuild for updated spec-helper

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 408771
- adding missing buildrequires:
- rebuild using %%perl_convert_version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix spacing at top of description
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jun 21 2007 Michael Scherer <misc@mandriva.org> 0.04-2mdv2008.0
+ Revision: 41991
- rebuild


* Sat Feb 04 2006 Michael Scherer <misc@mandriva.org> 0.04-1mdk
- First Mandriva package, fix #21014

