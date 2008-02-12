%define realname   Devel-Profiler

Name:		perl-%{realname}
Version:    0.04
Release:    %mkrel 2
License:	GPL and Artistic
Group:		Development/Perl
Summary:    A Perl profiler compatible with dprofpp  
Source0:    http://search.cpan.org/CPAN/authors/id/S/SA/SAMTREGAR/Devel-Profiler-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildArch: noarch

%description
This module implements a Perl profiler that outputs profiling data in
a format compatible with "dprofpp", Devel::DProf's profile analysis
tool.  It is meant to be a drop-in replacement for Devel::DProf.

NOTE: If Devel::DProf works for your application then there is no
reason to use this module.


%prep
%setup -q -n Devel-Profiler-%{version} 
# broken http://rt.cpan.org/Public/Bug/Display.html?id=7400
rm -f t/01basic.t

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

