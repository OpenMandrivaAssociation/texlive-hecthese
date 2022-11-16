Name:		texlive-hecthese
Version:	60455
Release:	1
Summary:	A class for dissertations and theses at HEC Montreal
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hecthese
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hecthese.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hecthese.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hecthese.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the hecthese class, a class based on
memoir and compatible with LaTeX. Using this class,
postgraduate students at HEC Montreal will be able to write
their dissertation or thesis while complying with all the
presentation standards required by the University. This class
is meant to be as flexible as possible; in particular, there
are very few hardcoded features except those that take care of
the document's layout. Dissertations and theses at HEC Montreal
can be written on a per-chapter or per-article basis. Documents
that are written on a per-article basis require a bibliography
for each of the included articles and a general bibliography
for the entire document. The hecthese class takes care of these
requirements. The class depends on babel, color, enumitem,
fontawesome, framed, numprint, url, and hyperref.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hecthese
%{_texmfdistdir}/tex/latex/hecthese
%doc %{_texmfdistdir}/doc/latex/hecthese

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
