import { library } from '@fortawesome/fontawesome-svg-core'
import {
  faChevronDown,
  faAngleDown
} from '@fortawesome/free-solid-svg-icons'

export const fontAwesomeInitialize = () => {
  return library.add(
    faChevronDown,
    faAngleDown
  )
}