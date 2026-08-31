#include "rclcpp/rclcpp.hpp"
#include "stereo-slam-node.hpp"
#include <algorithm>
#include <cctype>
#include <chrono>
#include <fstream>
#include <iostream>
#include <string>

#include "System.h"

int
main(int argc, char** argv)
{
  if (argc < 4) {
    std::cerr
      << "\nUsage: ros2 run orbslam stereo path_to_vocabulary path_to_settings do_rectify"
      << std::endl;
    return 1;
  }

  rclcpp::init(argc, argv);

  std::string vis_arg = argv[5];
  std::transform(vis_arg.begin(), vis_arg.end(), vis_arg.begin(), [](unsigned char c) {
    return std::tolower(c);
  });
  bool visualization = (vis_arg == "true" || vis_arg == "1");

  ORB_SLAM3::System pSLAM(argv[1], argv[2], ORB_SLAM3::System::STEREO, visualization);

  auto node = std::make_shared<StereoSlamNode>(&pSLAM, argv[2], argv[3]);
  std::cout << "============================ " << std::endl;

  rclcpp::spin(node);
  rclcpp::shutdown();

  return 0;
}
