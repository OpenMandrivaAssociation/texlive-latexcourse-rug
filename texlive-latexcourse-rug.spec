Name:		texlive-latexcourse-rug
Version:	39026
Release:	1
Summary:	A LaTeX course book
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latexcourse-rug
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcourse-rug.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexcourse-rug.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the book and practice files for a LaTeX
course that the author has give several times at the
Rijksuniversiteit Groningen (Netherlands).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/latexcourse-rug

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
