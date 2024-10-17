%bcond_with bootstrap
%global packname  PBSmapping
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.65.40
Release:          2
Summary:          Mapping Fisheries Data and Spatial Analysis Tools
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/PBSmapping_2.65.40.tar.gz
Requires:         R-foreign R-deldir
%if %{without bootstrap}
Requires:         R-maptools
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-foreign R-deldir
%if %{without bootstrap}
BuildRequires:    R-maptools
%endif

%description
This software has evolved from fisheries research conducted at the Pacific
Biological Station (PBS) in Nanaimo, British Columbia, Canada. It extends
the R language to include two-dimensional plotting features similar to
those commonly available in a Geographic Information System (GIS). 
Embedded C code speeds algorithms from computational geometry, such as
finding polygons that contain specified point events or converting between
longitude-latitude and Universal Transverse Mercator (UTM) coordinates. 
It includes data for a global shoreline and other data sets in the public
domain. The R directory '.../library/PBSmapping/doc' includes a complete
user's guide PBSmapping-UG.pdf. To use this package effectively, please
consult the guide.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/Extra
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/Utils
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
