/*
 * Copyright 2011 Inalogic® Inc.
 *
 * This program is free software: you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License, as
 * published by the  Free Software Foundation; either version 2.1 or 3.0
 * of the License.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranties of
 * MERCHANTABILITY, SATISFACTORY QUALITY or FITNESS FOR A PARTICULAR
 * PURPOSE.  See the applicable version of the GNU Lesser General Public
 * License for more details.
 *
 * You should have received a copy of both the GNU Lesser General Public
 * License along with this program. If not, see <http://www.gnu.org/licenses/>
 *
 * Authored by: Tim Penhey <tim.penhey@canonical.com>
 *
 */
#ifndef OPENASR_TESTS_FILE_HELPERS_H
#define OPENASR_TESTS_FILE_HELPERS_H

#include <string>
#include <sstream>

namespace openasr
{
namespace testing
{

class CaptureLogOutput
{
public:
  CaptureLogOutput();
  ~CaptureLogOutput();
  std::string GetOutput();
private:
  std::ostringstream sout_;
};

}
}

#endif
