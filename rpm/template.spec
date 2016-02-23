Name:           ros-jade-rail-pick-and-place-tools
Version:        1.1.9
Release:        0%{?dist}
Summary:        ROS rail_pick_and_place_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rail_pick_and_place_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       ros-jade-actionlib
Requires:       ros-jade-graspdb
Requires:       ros-jade-rail-grasp-collection
Requires:       ros-jade-rail-pick-and-place-msgs
Requires:       ros-jade-rail-recognition
Requires:       ros-jade-roscpp
Requires:       ros-jade-rviz
Requires:       ros-jade-std-srvs
BuildRequires:  boost-devel
BuildRequires:  ros-jade-actionlib
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-graspdb
BuildRequires:  ros-jade-rail-pick-and-place-msgs
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rviz
BuildRequires:  ros-jade-std-srvs

%description
RViz Plugins for Collecting Grasps and Generating Models

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Feb 23 2016 David Kent <dekent@gatech.edu> - 1.1.9-0
- Autogenerated by Bloom

* Tue Aug 18 2015 David Kent <davidkent@wpi.edu> - 1.1.8-0
- Autogenerated by Bloom

* Fri May 08 2015 David Kent <davidkent@wpi.edu> - 1.1.7-0
- Autogenerated by Bloom

* Tue May 05 2015 David Kent <davidkent@wpi.edu> - 1.1.6-0
- Autogenerated by Bloom

* Mon May 04 2015 David Kent <davidkent@wpi.edu> - 1.1.5-0
- Autogenerated by Bloom

