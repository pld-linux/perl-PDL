Summary:	perlDL
Summary(pl):	perlDL
Name:		perl-PDL
Version:	2.002
Release:	2
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Copyright:	GPL
URL:		http://www.perl.com/CPAN//modules/by-module/PDL/PDL-%{version}.readme
Source:		ftp://ftp.digital.com/pub/plan/perl/CPAN/modules/by-module/PDL/PDL-%{version}.tar.gz
Patch0:		perl-PDL-conf.patch
Patch1:		perl-PDL-doc.patch
Patch2:		perl-PDL-die_where.patch
Patch3:		perl-PDL-croak.patch
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	Mesa-devel
BuildRequires:	XFree86-devel
BuildRequires:	ncurses-devel
%requires_eq	perl
Requires:	%{perl_sitearch}
Buildroot:	/tmp/%{name}-%{version}-root

%description
The perlDL project aims to turn perl into an efficient numerical language for
scientific computing. The PDL module gives standard perl the ability to
COMPACTLY store and SPEEDILY manipulate the large N-dimensional data sets which
are the bread and butter of scientific computing. e.g. C<$a=$b+$c> can add two
2048x2048 images in only a fraction of a second.


%description -l pl
perlDL rozsze¿a mo¿liwo¶ci perl'a o funkcje do obliczeñ numerycznych 
i naukowaych.

%prep
%setup  -q -n PDL-%{version}
%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS -I/usr/include/ncurses -DNCURSES -DPERL_POLLUTE" 

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man{1,3}/*

find $RPM_BUILD_ROOT%{perl_sitearch}/auto/PDL -name \*.so -exec \
	strip --strip-unneeded {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%{perl_sitearch}/PDL
%{perl_sitearch}/PDL.pm
%attr(-,root,root) %{perl_sitearch}/auto/PDL
