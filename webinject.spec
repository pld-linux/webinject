# TODO
# - needs fixes as the program attempts to write tmp files as dirname($0)/tmp.$$.tmp !!!
%include	/usr/lib/rpm/macros.perl
Summary:	Tool for automating tests of web applications and services
Name:		webinject
Version:	1.35
Release:	0.9
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/webinject/%{name}-%{version}.src.tar.gz
# Source0-md5:	d2d7e3cd7063d1cd5ac11507871ac196
Patch0:		%{name}-fixes.patch
URL:		http://www.webinject.org/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}

%description
WebInject is a free tool for automated testing of web applications and
services. It can be used to test individual system components that
have HTTP interfaces (JSP, ASP, CGI, PHP, Servlets, HTML Forms, etc),
and can be used as a test harness to create a suite of [HTTP level]
automated functional, acceptance, and regression tests. A test
harness, also referred to as a test driver or a test framework, allows
you to run many test cases and collect/report your results. WebInject
offers real-time results display and may also be used for monitoring
system response times. 

WebInject can be used as a complete test framework that is controlled
by the WebInject User Interface (GUI). Optionally, it can be used as a
standalone test runner (text/console application) which can be
integrated and called from other test frameworks or applications.

%package gui
Summary:	Webinject GUI
Group:		Applications/Web
# not autodetected
Requires:	perl-Tk-ProgressBar-Mac

%description gui
GUI Tool for webinject.

%prep
%setup -q -n %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir}}

install %{name}.pl $RPM_BUILD_ROOT%{_bindir}
install %{name}gui.pl $RPM_BUILD_ROOT%{_bindir}
install config.xml $RPM_BUILD_ROOT%{_sysconfdir}
install testcases.xml $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/webinject.pl

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/webinjectgui.pl
